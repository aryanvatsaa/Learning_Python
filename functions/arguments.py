#Keyword Arguments : - 
# In Python, keyword arguments allow you to specify the values of function parameters by explicitly naming them in the function call. This allows you to pass arguments in any order, as long as you use the correct parameter names.


# Default Arguments : - 
# Python allows users to specify function arguments with default values. This means that if the user does not provide a value for that argument, the function will use the default value instead.

#Example :-
# def display(name, course = "Btech"):
#     print("Name : " + name)
#     print("Course : " + course)
# display(course="BCA", name="Aryan")     # Keyword Arguments
# display(name="Reyansh")                 # Default arguments for course.

# Variable-length Arguments : -
# In Python, variable-length arguments allow you to pass a variable number of arguments to a function. This is useful when you don't know in advance how many arguments will be passed to the function. There are two types of variable-length arguments: *args and **kwargs.

#Example of *args :-
# def sum_numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
# sum = sum_numbers(1, 2, 3, 4, 5)
# print(sum)  # Output: 15

#Example of **kwargs :-
# def display_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# display_info(name="Aryan", age=20, course="Btech")

