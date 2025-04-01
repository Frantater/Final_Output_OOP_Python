class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"

class SchoolBus(Vehicle):
    def __init__(self, brand, model, year, capacity):
        super().__init__(brand, model, year)
        self.capacity = capacity
    
    def display_info(self):
        return f"{super().display_info()} with capacity {self.capacity} students"

print("--- Checking if SchoolBus is an instance of Vehicle ---")
bus1 = SchoolBus("Ford", "Transit", 2022, 50)
bus2 = SchoolBus("Mercedes", "Sprinter", 2023, 40)
print(isinstance(bus1, Vehicle))  # True
print(isinstance(bus2, Vehicle))  # True

print("\n--- Employee Class with Multiple Constructors ---")
class Employee:
    def __init__(self, name=None, age=None, position=None):
        self.name = name if name else "Unknown"
        self.age = age if age else 0
        self.position = position if position else "Unassigned"
    
    def display_info(self):
        return f"Employee: {self.name}, Age: {self.age}, Position: {self.position}"

    @staticmethod
    def create_employee_from_string(employee_string):
        name, age, position = employee_string.split(',')
        return Employee(name.strip(), int(age.strip()), position.strip())

    @classmethod
    def create_employee_from_data(cls, name, age, position):
        return cls(name, age, position)

emp1 = Employee("Alice", 30, "Manager")
emp2 = Employee("Bob")
emp3 = Employee.create_employee_from_string("Charlie, 25, Developer")
emp4 = Employee.create_employee_from_data("Dave", 35, "HR")

print(emp1.display_info())
print(emp2.display_info())
print(emp3.display_info())
print(emp4.display_info())

print("\n--- School Classes Displaying Average Grades and GPA ---")
class School:
    class Grade:
        def __init__(self, subject, score):
            self.subject = subject
            self.score = score
        
        def display_grade(self):
            return f"{self.subject}: {self.score}"
    
    def __init__(self, name, students_grades):
        self.name = name
        self.students_grades = students_grades
    
    def average_grade(self):
        return sum(self.students_grades) / len(self.students_grades)
    
    def display_info(self):
        return f"{self.name} Average Grade: {self.average_grade():.2f}"

    @staticmethod
    def total_students(school_list):
        return sum(len(school.students_grades) for school in school_list)

school_one = School("CIIT", [85, 90, 78, 92])
school_two = School("DLSU", [88, 76, 95, 89])
school_three = School("UST", [80, 85, 88, 92])
print(school_one.display_info())
print(school_two.display_info())
print(school_three.display_info())
print(f"Total students in all schools: {School.total_students([school_one, school_two, school_three])}")

print("\n--- Operator Overloading with Vector Class ---")
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = Vector(1, 1)
v4 = v1 + v2
v5 = v2 + v3
print(v4)
print(v5)

print("\n--- Composition Over Inheritance: Book and Author Classes ---")
class Author:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display_info(self):
        return f"Book: {self.title}, Author: {self.author}"

author1 = Author("George Orwell")
author2 = Author("J.K. Rowling")
book1 = Book("1984", author1)
book2 = Book("Harry Potter", author2)
print(book1.display_info())
print(book2.display_info())
