#USEFUL FUNCTIONS :-
#find(str, beg, end) :- check if str is present in string.

# message = "She is my best friend."
# print(message.find("my", 0, len(message)))

#count(str, beg, end) :- count number of time str occurs in a string.

# str = "he"
# message = "helloworldhellohello"
# print(message.count(str,0,len(message)))

#center(width, fillcharr) :- returns a string with the original string centered to a total of width columns and filled with fillchar in columns.

# str = "hello"
# print(str.center(11, '*'))

#lower() //  upper() :- converts all characters in the string into lowercase//uppercase

# str = "Hello, Welcome to Python World!!"
# print(str.lower())
# print(str.upper())

#replace(old, new [, max]) :- replaces all or max occurences of old in strings with new.

# str = "hello hello hello"
# print(str.replace("he", "FO"))

#title() :- Returns string in title case.

# str = "The world is beautiful"
# print(str.title())

#swapcase() :- converts uppercase into lowercase and vice-versa.

# str = "The World Is Beautiful"
# print(str.swapcase())