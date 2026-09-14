# METHODS : - METHODS ARE FUNCTIONS THAT ARE DEFINED INSIDE A CLASS AND ARE USED TO PERFORM OPERATIONS ON OBJECTS OF THAT CLASS. THEY CAN ACCESS AND MODIFY THE ATTRIBUTES OF THE OBJECTS.


#1. INSTANCE METHODS : - Instance methods are the most common type of method. They are bound to a specific object (instance) created from the class and can freely access or modify that specific object's data.

#EX:-

# class Dog:
#     def __init__(self, name):
#         self.name = name             # Instance attribute

#     # Instance method
#     def bark(self):
#         return f"{self.name} says Woof!"

# # Usage
# my_dog = Dog("Buddy")
# print(my_dog.bark())  


#2. STATIC METHODS : - STATIC METHODS ARE METHODS THAT BELONG TO THE CLASS RATHER THAN AN INSTANCE OF THE CLASS. THEY DO NOT HAVE ACCESS TO THE INSTANCE (SELF) OR CLASS (CLS) VARIABLES. THEY ARE DEFINED USING THE @staticmethod DECORATOR.

#SYNATX :-

# @staticmethod
# def name(args...):
#     statements

#EX:- 

# class Example:
    
#     @staticmethod               #decorator
#     def hello():                   #doesn't use self parameter
#         print("Hello World !!")

# Example.hello()


#3. CLASS METHODS : - CLASS METHODS ARE METHODS THAT BELONG TO THE CLASS AND HAVE ACCESS TO THE CLASS VARIABLES. THEY ARE DEFINED USING THE @classmethod DECORATOR AND TAKE A CLASS PARAMETER (CLS) AS THEIR FIRST ARGUMENT.

#EX:-

# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         return self.length * self.breadth

#     @classmethod
#     def square(cls, side):
#         return cls(side, side)

# S = Rectangle.square(10)
# print("AREA = ", S.area())