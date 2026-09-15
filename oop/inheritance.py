# INHERITANCE : - ALLOWS A CLASS (CHILD CLASS) TO INHERIT ATTRIBUTES AND METHODS FROM ANOTHER CLASS (PARENT CLASS). THIS PROMOTES CODE REUSABILITY AND ESTABLISHES A HIERARCHICAL RELATIONSHIP BETWEEN CLASSES.


#1. SINGLE INHERITANCE :- ONE PARENT CLASS AND ONE CHILD CLASS

# class Animal:                                       # Parent Class
#     def __init__(self, name):
#         self.name = name   

#     def eat(self):
#         return f"{self.name} is eating."

# class Cat(Animal):                                # Child Class inheriting from Animal
#     def Meow(self):
#         return f"{self.name} says Meow!"

# my_cat = Cat("Cutie")
# print(my_cat.eat())                    # Inherited method 
# print(my_cat.Meow())                   # Child method     


#2. MULTIPLE INHERITANCE :- WHEN A DERIVED CLASS INHERITS FEATURES FROM MORE THAN ONE BASE CLASS IT IS CALLED MULTIPLE INHERITANCE.

#SYNTAX:-
# class Base1:
#     statement block 
# class Base2:
#     statement block 
# class Derived(Base1, Base2):
#     statement block 

# EX:-

# class First:
#     first = "First Class"

# class Second:
#     second = "Second Class"

# class Third(First, Second):
#     third = "Third Class"

# # Verification
# third1 = Third()
# print(third1.third)
# print(third1.second)
# print(third1.first)


#3. MULTI-LEVEL INHERITANCE :- DERIVING A CLASS FROM AN ALREADY DERIVED CLASS.

#SYNTAX :-
# class Base:
#     pass
# class Derived1(Base):
#     pass
# class Derived2(Derived1):
#     Pass

#EX:-

# class Person:
#     def name(self):
#         print("Name....")
# class Teacher(Person):
#     def Qualification(self):
#         print("Qualification...Ph.D must")
# class HOD(Teacher):
#     def experience(self):
#         print("Experience....at least 15 years")

# hod = HOD()
# hod.name()
# hod.Qualification()
# hod.experience()

#Q. WAP THAT HAS A CLASS PERSON. INHERIT A CLASS FACULTY FROM PERSON WHICH ALSO HAS A CLASS PUBLICATIONS.

class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def display(self):
        print("NAME : ", self.name)
        print("AGE : ", self.age)
        print("SEX : ", self.sex)

class Publications:
    def __init__(self, no_RP, no_Books, no_Art):
        self.no_RP = no_RP
        self.no_Books = no_Books
        self.no_Art = no_Art
    def display(self):
        print("Number of Research papers Published : ", self.no_RP)
        print("Number of Books Published : ", self.no_Books)
        print("Number of Articles Published : ", self.no_Art)

class Faculty(Person):
    def __init__(self, name, age, sex, desig, dept, no_RP, no_Books, no_Art):
        Person.__init__(self, name, age, sex)
        self.desig = desig
        self.dept = dept
        self.Pub = Publications(no_RP, no_Books, no_Art)
    def display(self):
        Person.display(self)
        print("DESIGNATION : ", self.desig)
        print("DEPARTMENT : ", self.dept)
        self.Pub.display()

F = Faculty("Aryan", 36, "Male", "TIC", "Computer Science", 22, 1, 3)
F.display()
F = Faculty("Ananya", 36, "Female", "TIC", "Maths", 10, 12, 5)
F.display()
F = Faculty("Saket", 33, "Male", "TIC", "Economics", 36, 8, 2)
F.display()

