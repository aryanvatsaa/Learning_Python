#LOOPS THAT CAN BE INSIDE LOOPS ARE CALLED NESTED LOOPS. THE INNER LOOP IS EXECUTED COMPLETELY FOR EVERY ITERATION OF OUTER LOOP. 
#SYNTAX :-
# for variable in sequence:
#     for variable in sequence:
#         # code block to be executed for each iteration of the outer loop
# code block to be executed for each iteration of the outer loop

#Q1.  WAP TO PRINT THESE FOLLOWING PATTERN USING NESTED LOOPS.
# *****                                      #1 2 3 4 5
# *****                                      #1 2 3 4 5
# *****                                      #1 2 3 4 5
# *****                                      #1 2 3 4 5
# *****                                      #1 2 3 4 5
# for i in range(5):                    #FOR ASTERIKS
#     for j in range(5):
#         print("*", end=" ")
#     print()  # Move to the next line after each row

# for i in range(1,6):                      #FOR NUMBERS
#     for j in range(1,6):
#         print(j, end=" ")
#     print()  # Move to the next line after each row


# Q2. WAP TO PRINT THE FOLLOWING PATTERN USING NESTED LOOPS.
# *                                            # 1
# * *                                          # 1 2
# * * *                                        # 1 2 3
# * * * *                                      # 1 2 3 4
# * * * * *                                    # 1 2 3 4 5

# for i in range(1,6):                    #FOR ASTERIKS
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()  # Move to the next line after each row

# for i in range(1,6):                        #FOR NUMBERS
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()  # Move to the next line after each row

# Q3. WAP TO PRINT THE FOLLOWING NUMERICAL PYRAMID PATTERN USING NESTED LOOPS. 
#                    1
#                  1 2 1
#                1 2 3 2 1
#              1 2 3 4 3 2 1
#            1 2 3 4 5 4 3 2 1

# n = 5
# for i in range(1, n + 1):                   # Print leading spaces
#     for j in range(n - i):                  
#         print(" ", end=" ")                 # Print increasing numbers
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     for j in range(i - 1, 0, -1):           # Print decreasing numbers
#         print(j, end=" ")
#     print()  # Move to the next line after each row