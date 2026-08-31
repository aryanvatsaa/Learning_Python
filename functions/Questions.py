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