#LISTS :- Lists are mutable, ordered sequences of elements. They can contain elements of different data types, including other lists separated by commas. Lists are defined using square brackets []. Similar to strings, lists can be indexed and sliced but Lists are mutable, meaning their elements can be changed after they are created.

#list = ['a', 'bc', 78, 1.23]
# list2 = ['d', 78]
# print(list)
# print(len(list))                          #Prints length of list
# print(list*2)                          #Prints list two times
# print(list[0])                          #Prints first element of list
# print(list[1:3])                        #Prints elements from index 1 to 2
# print(list[2:])                          #Prints elements from index 2 to end
# list[0] = 'A'                            #Changes first element of list
# print(list)
# print(list + list2)                          #Concatenates two lists

# LISTS METHODS :-
#i. list.append() - Adds an element at the end of the list
# list = ['a', 'bc', 78, 1.23]
# list.append('d')
# print(list)

#ii. list.sort() - sorts in ascending order
#    list.sort(reverse=True) - sorts in descending order
# list = [1, 5, 3, 2, 4]
# list.sort()
# print(list)

#iii. list.reverse() - reverses the order of the list
# list = [1, 5, 3, 2, 4]
# list.reverse()
# print(list)

# iv. list.insert(index, element) - inserts an element at a given index
# list = ['a', 'bc', 78, 1.23]  
# list.insert(1, 'd')
# print(list)

# v. list.pop() - Removes the last object, if provided index it will remove element from given index
# list = [1, 5, 3, 2, 4]
# list.pop([3])
# list.pop()
# print(list)

# vi. list.remove(element) - Remvoes the element from the list
# list = [1, 5, 3, 2, 4]
# list.remove(5)
# print(list)



#TUPLES - Tuples are immutable, ordered sequences of elements. They can contain elements of different data types, including other tuples separated by commas. Tuples are defined using parentheses (). Similar to strings and lists, tuples can be indexed and sliced but cannot be modified after creation.

#tup = (1, 2, 3, 4)
# print(tup)
# print(type(tup))
# tup1 = (1)
# print(type(tup1))                          #This is not a tuple, it is an integer
# tup2 = (1,)                                #Comma is necessary to create a tuple with a single element
# print(type(tup2))                          #This is a tuple
##print(len(tup))                          #Prints length of tuple

# REST TUPLE METHODS ARE SIMILAR TO LIST METHODS EXCEPT FOR APPEND, INSERT, REMOVE, POP, SORT, REVERSE AS TUPLES ARE IMMUTABLE.


# PRACTICE -------------

# Q1. WAP TO ASK USER TO ENTER NAMES OF THREE FAVORITE MOVIES & STORE THEM IN THE LIST.

# movies = []
# mov1 = input("Enter 1st Movie : ")
# mov2 = input("Enter 2nd Movie : ")
# mov3 = input("Enter 3rd Movie : ")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

# Q2. WAP TO CHECK IF A LIST CONTAINS PALINDROME OF ELEMENTS.

# list1 = [1,2,1]
# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# list2 = [1,2,3]
# copy_list2 = list2.copy()
# copy_list2.reverse()

# if(copy_list2 == list2):
#     print("Palindrome")
# else:
#     print("Not Palindrome")