# FUNCTIONS :- A FUNCTION IS A BLOCK OF ORGANIZED AND REUSABLE CODE THAT IS USED TO PERFORM A SINGLE, RELATED ACTION. FUNCTIONS PROVIDE BETTER MODULARITY FOR YOUR APPLICATION AND A HIGHER DEGREE OF CODE REUSE.

#SYNTAX OF FUNCTION IN PYTHON :-
#def function_name(parameters):
#    #function body
#return value

#RETURN STATEMENT :- The return statement is used to exit a function and go back to the place where it was called. This statement can optionally return a value to the caller. A return statement with no arguments is the same as return None.

#EXAMPLE OF FUNCTION IN PYTHON :-
# def add_numbers(a, b):               # a and b are parameters
#     return a + b
# result = add_numbers(3, 5)           # function call with arguments 3 and 5
# print(result)                        # This will print 8

#Q1. WAP TO CALCULATE AVERAGE OF TWO NUMBERS USING FUNCTION IN PYTHON.
# def calc_avg(a, b, c):
#     sum = a+b+c
#     avg = sum/3
#     return avg
# avg = calc_avg(10,20,30)
# print(avg)

#Q2. WAFunction TO PRINT THE LENGTH OF A LIST.
# names = ["Aryan", "Arya", "John"]
# def print_len(list):
#     print(len(list))

# print_len(names)

#Q3. WAF TO CONVERT FROM USD TO INR.
# inr = float(input("Enter the amount in USD: "))
# def function(inr):
#     usd_inr = inr * 95.26
#     return usd_inr
# convert = function(inr)
# print(convert)

#Q4. WAF TO FIND THE FACTORIAL OF N (N IS THE PARAMETER OF FUNCTION).
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))  