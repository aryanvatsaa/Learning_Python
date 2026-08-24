#Arithmetic, Comparison, Assignment, Logical, Unary, Bitwise, Membership, Identity Operators

#1. Arithmetic Operators are +, -, *, /, %, **, //
# a = 50
# b = 25
# print(a + b)
# print(a - b)
# print(a * b)                                #Multiply
# print(b / a)                                #Divide
# print(a % b)                                #Remainder
# print(a ** b)                               #Exponent
# print(a // b)                               #Floor Divison

#2. Comparison OR relational operators are ==, !=, >, <, >=, <= . Returns boolean values in true/false.
# a = 100
# b = 50
# print(a == b)                                #Equal to
# print(a != b)                                #Not Equal to
# print(a > b)                                 #Greater than
# print(a < b)                                 #Less than
# print(a >= b)                                #Greater than or equal to
# print(a <= b)                                #Less than or equal to

#3. Assignment operators are =, +=, -=, *=, /=, %=, //=, **=
num = 10
num += 5
print("num : ", num)                                      #15
num -= 5
print("num : ", num)                                      #10
num *= 5
print("num : ", num)                                      #50
num /= 5
print("num : ", num)                                      #10.0

#4. Bitwise operators are AND(&), OR(|), XOR(^), NOT(~)

#5. Logical operators are AND(&&), OR(||), NOT(!)
a = 50
b = 30
print(a > b and a != b)                                   #True
print(a > b or a == b)                                    #True