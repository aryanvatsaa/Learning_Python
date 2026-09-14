# CLASS :- A blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).

# OBJECTS :- An object is an instance of a class. It is a self-contained entity that consists of both data and procedures to manipulate the data. Objects are created from classes and can have unique attributes and behaviors.

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.


# DEFINING CLASSES AND CREATING OBJECTS :-
# class class_name:
#     <statement - 1>
#     <statement - 2>
#     .
#     .
#     <Statement - N>
# object_name = class_name
# object_name.class_member_name

# class ABC:              #creating class
#     var = 10            #class variable
# obj = ABC()
# print(obj.var)          #class variable is accessed using class object

# Q1. WAP THAT USES CLASS TO STORE THE NAME AND MARKS OF STUDENTS. USE LIST TO STORE THE MARKS IN THREE SUBJECTS.

# class Students:
#     def __init__(self, name):
#         self.name = name
#         self.marks = []

#     def enterMarks(self):
#         for i in range(3):
#             m = int(input("Enter the marks of %s in subject %d : "% ( self.name , i+1 )))
#             self.marks.append(m)

#     def display(self):
#         print(self.name, " got ", self.marks)

# s1 = Students("Aryan")
# s1.enterMarks()
# s2 = Students("Arya")
# s2.enterMarks()
# s1.display()
# s2.display()

#Q2. WAP THAT HAS A CLASS FRACTION WITH ATTRIBUTES NUMERATOR AND DENOMINATOR. ENTER THE VALUES OF THE ATTRIBUTES AND PRINT THE FRACTION IN THE SIMPLIFIED FORM.

# class fraction:
#     def get_data(self):
#         self.__num = int(input("Enter the numerator : "))
#         self.__deno = int(input("Enter the denominator : "))
#         if(self.__deno == 0):
#             print("Fraction not possible")
#             exit()

#     def display_data(self):
#         self.__simplify()
#         print(self.__num, "/", self.__deno)

#     def __simplify(self):
#         print("The simplified fraction is : ")
#         common_divisor = self.__GCD(self.__num, self.__deno)
#         self.__num = self.__num/common_divisor
#         self.__deno = self.__deno/common_divisor

#     def __GCD(self, a, b):
#         if(b==0):
#             return a
#         else:
#             return self.__GCD(b, a%b)

# f = fraction()
# f.get_data()
# f.display_data()

#Q3. WAP TO DEPOSIT OR WITHDRAW MONEY IN A BANK ACCOUNT.

# class Account:
#     def __init__(self):
#         self.balance = 0
#         print("New Account Created : ")

#     def deposit(self):
#         amount = float(input("Enter amount to deposit : "))
#         self.balance += amount
#         print("New Balance : ", self.balance)

#     def withrdraw(self):
#         amount = float(input("Enter amount to withdraw : "))
#         if(amount > self.balance):
#             print("Insufficient Balance !!")
#         else:
#             self.balance -= amount
#             print("New Balance : ", self.balance)

#     def enquiry(self):
#         print("Balance : ", self.balance)

# account = Account()
# account.deposit()
# account.withrdraw()
# account.enquiry()
