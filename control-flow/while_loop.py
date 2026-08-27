#WHILE LOOP :- PROVIDES A MECHANISM TO REPEAT ONE OR MORE STATEMENTS UNTIL A PARTICULAR CONDITION IS MET. SYNTAX :-
##SYNATX :-
# while condition:
#     # code block to be executed until the condition is true

#Q1. WAP TO CALCULATE THE SUM OF NUMBERS FROM M-N.
# m = int(input("Enter the value of m : "))
# n = int(input("Enter the value of n : "))
# sum = 0
# i = m
# while i <= n:
#     sum += i
#     i += 1
# print("The sum of numbers from", m, "to", n, "is :", sum)

#Q2. WAP TO ENTER A NUMBER AND THEN CALUCLATE THE SUM OF DIGITS OF THAT NUMBER.
# num = int(input("Enter a number : "))
# sum_of_digits = 0
# while num != 0:
#     temp = num % 10
#     sum_of_digits = sum_of_digits + temp
#     num = num // 10
# print("The sum of digits is :", sum_of_digits)

#Q3. WAP TO PRINT THE REVERSE OF A NUMBER ENTERED BY THE USER.
num = int(input("Enter a number : "))
reverse = 0
while num != 0:
    temp = num % 10
    reverse = reverse * 10 + temp
    num = num // 10
print("The reverse of the number is : ", reverse)