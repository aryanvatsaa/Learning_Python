#BREAK : - BREAK STATEMENT IS USED TO TERMINATE THE LOOP AND TRANSFER THE CONTROL TO THE STATEMENT IMMEDIATELY FOLLOWING THE LOOP.

#CONTINUE : - CONTINUE STATEMENT IS USED TO SKIP THE CURRENT ITERATION OF THE LOOP AND TRANSFER THE CONTROL TO THE NEXT ITERATION OF THE LOOP.

#Q1. WAP TO PRINT ALL THE NUMBERS FROM 1-10, EXCEPT 5.
# for i in range(1,11):
#     if(i==5):
#         continue                    #SKIPPED 5.
#     print(i, end=" ")
# print("\n Done")

#Q2. WAP THAT PROMPTS USERS TO ENTER NUMBERS. THE PROCESS WILL REPEAT UNTIL THE USER ENTERS -1. FINALLY, PROGRAM, PRINTS THE COUNT OF PRIME AND COMPOSITE NUMBERS ENTERED BY THE USER.

# prime_count = 0
# composite_count = 0
# n = int(input("Enter a number (-1 to exit): "))
# while(n != -1):
#     if(n < 2):
#         print(n, "is neither prime nor composite.")
#     else:
#         is_prime = True
#         for i in range(2, int(n**0.5) + 1):
#             if(n % i == 0):
#                 is_prime = False
#                 break
#         if(is_prime):
#             prime_count += 1
#             print(n, "is a prime number.")
#         else:
#             composite_count += 1
#             print(n, "is a composite number.")
#     n = int(input("Enter a number (-1 to exit): "))
# print("Count of prime numbers:", prime_count)
# print("Count of composite numbers:", composite_count)