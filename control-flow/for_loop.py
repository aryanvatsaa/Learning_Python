# FOR LOOP PROVIDES A MECHANISHM TO REPEAT A TASK UNTIL A PARTICULAR CONDITION IS MET. SYNTAX :-
# for variable in sequence:
#     # code block to be executed for each item in the sequence

#THE RANGE FUNCTION IS USED TO GENERATE A SEQUENCE OF NUMBERS. IT TAKES THREE PARAMETERS START, STOP AND STEP. THE START PARAMETER IS INCLUSIVE AND THE STOP PARAMETER IS EXCLUSIVE. THE STEP PARAMETER IS OPTIONAL AND IT DEFINES THE INCREMENT BETWEEN EACH NUMBER IN THE SEQUENCE.
#          range(start, stop, [step])

#Taking input and printing the elements in the list using for loop.
# n = int(input("Enter the number of elements in the list: "))  
# list = []
# for i in range(n):
#     element = input(f"Enter element {i+1}: ")
#     list.append(element)                               # Add the element to the list
# print("The final list is:")
# print(list)
# print("The elements in the list are:")
# for el in list:
#     print(el)

# Q1. WAP TO PRINT THE MULTIPLICATION TABLE ON N, WHERE N IS ENTERED BY THE USER.
# n = int(input("Enter a number: "))
# print("Multiplication table of ",n)
# for (i) in range(1,11):
#     print(n, "X",i,"=", n*i)

#Q2. WAP TO PRINT ALL THE NUMBERS FROM M-N THEREBY CLASSIFYING THEM AS EVEN OR ODD.
# m = int(input("Enter the value of m : "))
# n = int(input("Enter the value of n : "))
# for i in range(m, n+1):
#     if(i%2 == 0):
#         print(i, "is even number")
#     else:
#         print(i, "is odd number")

#Q3. WAP TO CALCULATE FACTORIAL OF A NUMBER.
# num = int(input("Enter the number : "))
# if(num==0):
#     fact = 1
# fact = 1
# for i in range(1,num+1):
#     fact = fact*i
# print("Factorial of ", num, " is ", fact)

#Q4. WAP THAT DISPLAYS ALL LEAP YEARS FROM 1900-2101.
# print("LEAP YEARS FROM 1900-2101 ARE : ")
# for i in range(1900,2101):
#     if(i%4==0):
#         print(i, end=' ')

#Q5. WAP TO CALCULATE THE SUM OF CUBES OF NUMBER 1-N.
# n = int(input("Enter the value of n : "))
# sum = 0
# for i in range(1,n+1):
#     a = i**3
#     sum = sum+a
# print("The sum of cubes is ", sum)

#Q6. WAP TO CALCULATE THE VALUE OF AN INVESTMENT. INPUT AN INITIAL VALUE OF INVESTMENT AND ANNUAL INTEREST, AND CALCULATE THE VALUE OF INVESTMENT OVER TIME.
# principal = float(input("Enter the principal Value : "))
# interest = float(input("Enter the rate of interest : "))
# time = int(input("Enter the number of years for which investment has to be done : "))
# amount = principal
# print("\tYear \t\t Value")
# print("-----------------------")
# for i in range(1, time+1):
#     amount = amount*(1+interest/100.0)
#     print(i," \t\t ",amount)

#Q7. WAP TO FIND SUM OF FIRST N NUMBERS.
# num = int(input("Enter a Number : "))
# sum = 0
# for i in range(1,num+1):
#     sum=sum+i
# print(sum)

