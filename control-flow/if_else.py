#if-else syntax :-

# if condition:
#     # code block to be executed if condition is true
# else:
#     # code block to be executed if condition is false


#Q1. WAP TO WHETHER A PERSON IS ELIGIBLE TO VOTE OR NOT.
# a  = int(input("Enter your age : "))
# if (a>=18):
#     print("You are eligible to vote !!")
# else:
#     print("You are not eligible to vote!!")

#Q2. WAP to check if a number is a multiple of 7 or not.
# num = int(input("Enter a Number : "))
# if (num % 7 == 0):
#     print("Multiple of 7 !!")
# else:
#     print("Not a Multiple of 7 !!")

#Q3. WAP to check if a number entered by the user is odd or even.
# num = int(input("Enter a Number : "))
# if (num % 2 == 0):
#     print("Even Number !!")
# else:
#     print("Odd Number !!")

# Nested if-else syntax :-
# if condition1:
#     if condition2:
#         # code block to be executed if condition1 and condition2 are true
#     else:
#         # code block to be executed if condition1 is true but condition2 is false
# else:
#     # code block to be executed if condition1 is false

#if-elif-else syntax :-
# if condition1:
#     # code block to be executed if condition1 is true
# elif condition2:
#     # code block to be executed if condition1 is false and condition2 is true
# else:
#     # code block to be executed if both condition1 and condition2 are false

#Q4. WAP TO TEST WHETHER A NUMBER ENTERED BY THE USER IS NEGATIVE, POSITIVE OR EQUAL TO ZERO.

# num = int(input("Enter any number : "))
# if(num == 0):
#     print("The value is equal to zero.")
# elif(num>0):
#     print("The number is positive.")
# else:
#     print("The number is Negative.")

#Q5. WAP TO FIND THE GREATEST NUMBER FROM THREE NUMBERS.

# num1 = int(input("Enter 1st Number : "))
# num2 = int(input("Enter 2nd Number : "))
# num3 = int(input("Enter 3rd Number : "))
# if num1 >= num2 and num1 >= num3:
#     print(num1, "is the greatest number.")
# elif num2 >= num1 and num2 >= num3:
#     print(num2, "is the greatest number.")
# else:
#     print(num3, "is the greatest number.")

#Q6. WAP TO DETERMINE WHETHER THE CHARACTER ENTEREDIS A VOWEL OR NOT.

# ch = input("Enter any character : ")
# if(ch=="A"or ch=="E" or ch=="I" or ch=="O" or ch=="U"):
#     print(ch, " is a vowel.")
# elif(ch=="a"or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
#     print(ch, " is a vowel.")
# else:
#     print(ch, " is not a vowel.")