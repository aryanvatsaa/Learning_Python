#Q1. WAP TO SWAP TWO NUMBERS.
# def swap(a,b):
#     a,b = b,a
#     print("After Swap : ")
#     print("First Number : ",a)
#     print("Second Number : ",b)

# a = input('Enter first Number : ')
# b = input("Enter Second Number : ")
# print("Before swap : ")
# print("First Number = ",a)
# print("Second Number = ",b)
# swap(a,b)

#Q2. WAP TO CONVERT TIME INTO MINUTES.
# def convert(hrs, min):
#     min = hrs*60+min
#     return min
# h = int(input("Enter the Hours : "))
# m = int(input("Enter the minutes : "))
# m = convert(h,m)
# print("Minutes : ",m)

#Q3. WAP THAT COMPUTES P(n,r).
# def fact(n):
#     f = 1
#     if(n==0 or n==1):
#         return 1
#     else:
#         for i in range(1,int(n+1)):
#             f = f*i
#     return f

# n = int(input("Enter the value of n : "))
# r = int(input("Enter the value of r : "))
# result = float(fact(n)) / float(fact(r))
# print("P(",str(n),"/",str(r),") = ",str(result))

#Q4. WAP TO PRINT FIBONACCI SERIES USING RECURSION.
# def fibonacci(n):
#     if(n<2):
#         return 1
#     return (fibonacci(n-1)+fibonacci(n-2))

# num1 = int(input("Enter the number of terms : "))

# for i in range(num1):
#     print("Fibonnaci(",i,") = ",fibonacci(i))

#Q5. WAP TO CONACATENATE TWO STRINGS USING RECUSION.
# def add(x,y):
#     z = x + y
#     return z
# str1 = str(input("Enter 1st string : "))
# str2 = str(input("Enter 2nd String : "))
# print(add(str1,str2))

#Q6. WAP TO FIND THE BIGGEST OF THREE INTEGERS USING FUNCTIONS.
# def biggest(num1,num2,num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
# x = int(input("Enter 1st Number : "))
# y = int(input("Enter 2nd Number : "))
# z = int(input("Enter 3rd Number : "))
# num4 = biggest(x,y,z)
# print("Biggest Number among entered three numbers : ", num4)

#Q7. WAF THAT ACCEPTS THREE INTEGERS, AND RETURNS TRUE IF ANY OF THE INTEGER IS 0, OTHERWISE IT RETURNS FALSE.
# def zero(x,y,z):
#     if(x == 0 or y == 0 or z == 0):
#         return True
#     else:
#         return False
# num1 = int(input("Enter 1st Number : "))
# num2= int(input("Enter 2nd Number : "))
# num3 = int(input("Enter 3rd Number : "))
# print(zero(num1,num2,num3))

#Q8. WAP TO PRINT ALL ELEMENTS IN A LIST USING RECURSIVE FUNCTIONS.
# def show (list):
#     for el in list:
#         print(el)
# list = ["Aryan", "Vatsa", 45]
# show(list)

#Q9. SHUFFLING A DECK OF CARDS USING RECURSION.
# import itertools, random
# deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))  #forming deck of cards
# random.shuffle(deck)                                   #shuffling cards
# print("Your Combination of cards is : ")               #printing shuffled five cards
# for i in range(5):
#     print(deck[i][0], "of", deck[i][1])

#Q10. TOWER OF HANOI
# def hanoi(n, A, B, C):                   #A,B AND C ARE POLES
#     if n>0:
#         hanoi(n - 1, A, C, B)
#         if A:
#             C.append(A.pop())
#         hanoi(n - 1, B, A, C)
# A = [1,2,3]                               # THREE RINGS ON THE 1ST POLE
# C = []
# B = []                                    # ALL THREE RINGS SHOULD MOVE TO 3RD POLE IN SAME ORDER AS 1ST POLE.
# hanoi(len(A),A,B,C)
# print(A,B,C)