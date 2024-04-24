class Person:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
    def display_attributes(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("ID:",self.id)
class Student(Person):
    def __init__(self, name, age, id,grade,classes):
        super().__init__(name, age, id)
        self.grade=grade
        self.classes=classes
    def display_attributes(self):
        super().display_attributes()
        print("grade:",self.grade)
        print("List of classes",self.classes)
class Teacher(Person):
    def __init__(self, name, age, id,subject,classes):
        super().__init__(name, age, id)
        self.subject=subject
        self.classes=classes
    def display_attributes(self):
        super().display_attributes()
        print("Subject:",self.subject)
        print("List of classes",self.classes)
class Administrator(Person):
    def __init__(self, name, age, id,department,employees):
        super().__init__(name, age, id)
        self.department=department
        self.employees=employees
    def display_attributes(self):
        super().display_attributes()
        print("Department:",self.department)
        print("List of employees",self.employees)
"""
student1=Student(input("enter student name"),input("enter age"),input("enter id"),input("enter grade"),["english","urdu","math","science"])
student2=Student(input("enter student name"),input("enter age"),input("enter id"),input("enter grade"),["english","urdu","math","science"])
student3=Student(input("enter student name"),input("enter age"),input("enter id"),input("enter grade"),["english","urdu","math","science"])
student4=Student(input("enter student name"),input("enter age"),input("enter id"),input("enter grade"),["english","urdu","math","science"])
student5=Student(input("enter student name"),input("enter age"),input("enter id"),input("enter grade"),["english","urdu","math","science"])
student6=Student(input("enter student name"),input("enter age"),input("enter id"),input("enter grade"),["english","urdu","math","science"])
student7=Student(input("enter student name"),input("enter age"),input("enter id"),input("enter grade"),["english","urdu","math","science"])
student8=Student(input("enter student name"),input("enter age"),input("enter id"),input("enter grade"),["english","urdu","math","science"])
student9=Student(input("enter student name"),input("enter age"),input("enter id"),input("enter grade"),["english","urdu","math","science"])
student0=Student(input("enter student name"),input("enter age"),input("enter id"),input("enter grade"),["english","urdu","math","science"])
student0.display_attributes()

teacher1=Teacher(input("enter teacher name"),input("enter age"),input("enter id"),input("enter subject"),[[student0,student1,student2],[student3,student4]])
teacher2=Teacher(input("enter teacher name"),input("enter age"),input("enter id"),input("enter subject"),[[student5,student6,student7],[student8,student9]])
teacher2.display_attributes()

admin1=Administrator(input("enter admin name"),input("enter age"),input("enter id"),input("enter department"),[teacher1,teacher2])
admin1.display_attributes()
"""