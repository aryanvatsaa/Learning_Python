# Polymorphism means "many forms". In OOP, it allows different classes to use the same method name, but each class can provide its own implementation.

# In Python, polymorphism is commonly seen in:
# 1. Method overriding
# 2. Duck typing
# 3. Operator overloading

# Example 1: Same method name, different behavior

# class Bird:
#     def fly(self):
#         print("Bird is flying")

# class Airplane:
#     def fly(self):
#         print("Airplane is flying")

# def make_it_fly(entity):
#     entity.fly()

# make_it_fly(Bird())
# make_it_fly(Airplane())
#print()

# Example 2: Polymorphism with method overriding

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")

# animals = [Dog(), Cat()]
# for animal in animals:
#     animal.sound()
# print()

# Example 3: Duck typing
# If an object has the required method, Python does not care about its class.

# class Person:
#     def speak(self):
#         print("Person speaks")

# class Speaker:
#     def speak(self):
#         print("Speaker speaks")

# def talk(obj):
#     obj.speak()

# talk(Person())
# talk(Speaker())
# print()

# Example 4: Operator overloading
# Python allows operators like + to behave differently for different classes.

# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return self.value + other.value

# n1 = Number(10)
# n2 = Number(20)

# print(n1 + n2)

