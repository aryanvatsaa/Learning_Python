#Q. WAP TO INPUT TWO NUMBERS AND CHECK WHETHER THEY ARE EQUAL OR NOT.
# n = int(input("Enter 1st Number : "))
# m = int(input("Enter 2nd number : "))
# if(m == n):
#     print("both numbers are equal.")
# else:
#     print("both numbers aren't equal.")

#Q. WAP TO FIND AVERAGE OF FIRST N NUMBERS USING FOR LOOP.
# n = int(input("Enter A Number : "))
# sum = 0
# for i in range(1, n+1):
#     sum = sum + i
# avg = sum/n
# print("SUM : ", sum)
# print("AVG : ", avg)

#Q. WAP TO GENERATE THIS PATTERN.
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# n = int(input("Enter the number of rows : "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if(i==1 or i==n or j==1 or j==n):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

#Q. WAP TO PRINT THE FIBONACCI SERIES UPTO N TERMS.
# Get the number of terms from the user
# n = int(input("Enter the number of terms: "))
# a, b = 0, 1                                             # First two terms
# if n <= 0:                                              # Check if the number of terms is valid
#     print("Please enter a positive integer.")
# elif n == 1:
#     print("Fibonacci series up to 1 term:")
#     print(a)
# else:
#     print("Fibonacci series:")
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b                                 # Update values for the next term
 