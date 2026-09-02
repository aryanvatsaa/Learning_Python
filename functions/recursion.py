# A RECURSIVE FUNCTION IS DEFINED AS A FUNCTION THAT CALLS ITSELD . EVERY RECURSIVE FUNCTIONS HAS TWO MAJOR CASES : -

# 1. BASE CASE :- IN WHICH THE PROBLEM IS SIMPLE ENOUGH TO BE SOLVED DIRECTLY WITHOUT MAKING ANY FURTHERS CALLS TO THE SAME FUCTION.
# 2. RECURSIVE CASE :- IN WHICH FIRSTLY THE PROBLEM IS DIVIDED INTO SUBPARTS. SECOND, THE FUNCTION CALLS ITSELF IN SUBPARTS. THIRD, THE RESULT IS OBTAINED BY COMBINING THE SOLUTIONS OF SIMPLE SUB-PARTS.

# EXAMPLE :- WAP TO PRINT NUMBERS FROM N TO 1.

# def show(num):
#     if num<=0:
#         return
#     print(num)
#     show(num-1)
# num = int(input('Enter first Number : '))
# show(num)

#Q1. WAP TO CALCULATE GCD USING RECURSIVE FUNCTIONS.
# def GCD(x,y):
#     rem = x%y
#     if(rem == 0):
#         return y
#     else:
#         return GCD(y, rem)
# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
# print("The GDC of number is", GCD(num1,num2))

#Q2. WAP TO CALCULATE EXPONENTS OF (X,Y) USING RECURSIVE FUNCTIONS.
# def exp(x,y):
#     if(y == 0):
#         return 1
#     else:
#         return(x*exp(x,y-1))
# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
# print("Result = ", exp(num1,num2))