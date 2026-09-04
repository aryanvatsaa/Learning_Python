#Q1. EAP TO PRINT THE FOLLOWIG PATTEN : -
#A
#AB
#ABC
#ABCD
#ABCDE
#ABCDEF
# for i in range(1,7):
#     ch = 'A'
#     print()
#     for j in range(1,i+1):
#         print(ch, end=' ')
#         ch = chr(ord(ch)+1)

#Q2. WAP THAT TAKES USER'S NAME AND PAN CARD NUMBER AS INPUT. VALIDATE THE INFORMATION USING ISX FUNCTION AND PRINT THE DETAILS.
# while(1):
#     name = input("Enter your name : ")
#     if name.isalpha() == False:
#         print("Invalid name, Sorry cannot proceed.")
#         break
#     else:
#         pan_card_no = input("Enter your PAN card number : ")
#         if pan_card_no.isalnum() == False:
#             print("Invalid PAN card number, Sorry you cannot proceed")
#             break
#     print("Please check, "+name+", your PAN card number is : " +pan_card_no)
#     break

#Q3. WAP TO THAT ENCRYPTS A MESSAGE BY ADDING A KEY VALUE TO EVERY CHARACTER. ( CAESAR CIPHER )
#HINT : SAY, IF KEY = 3, THEN ADD 3 TO EVERY CHARACTER IN THE MESSAGE.
# message = "HelloWorld"
# index = 0
# while index < len(message):
#     letter = message[index]
#     print(chr(ord(letter) + 3), end=' ')
#     index +=1

#Q4. WAP TO THAT ACCEPTS A STRING FROM USER AND REDISPLAYS THE SAME STRING AFTER REMOVING VOWELS FROM IT.
# def remove_vowels(s):
#     new_str = " "
#     for i in s:
#         if i in "aeiouAEIOU":
#             pass
#         else:
#             new_str += i
#     print("The string without vowels is : ", new_str)
# str = input("Enter a String : ")
# remove_vowels(str)

#Q5. WAP THAT COUNTS THE OCCURRENCES OF A CHARCTER IN A STRING. DO NOT USE BUILT-IN COUNT FUNCTIONS.
# def count_ch(s, c):
#     count = 0
#     for i in s:
#         if i == c:
#             count +=1
#     return compile
# str = input("Enter a String : ")
# ch = input("Enter the Character to be Searched : ")
# count = count_ch(str,ch)
# print("In ", str, ch, " occurs ", count, "times")

#Q5. WAP TO REVERSE A STRING.
# def reverse(str):
#     new_str = ' '
#     i = len(str)-1
#     while i>=0:
#         new_str += str[i]
#         i -= 1
#     return new_str

# str = input("Enter A string : ")
# print("The reversed String is : ", reverse(str))

#Q6. WAP TO PARSE AN EMAIL ID TO PRINT FROM WHICH EMAIL SERVER IT WAS SENT AND WHEN.

info = 'From aryanvatsa05@gmail.com Sun Oct 16 20:29:16 2016'
start = info.find('@') + 1
end = info.find(".com") +4
mailserver = info[start:end]
start = end + 1
end = len(info) - 1
date_time = info[start:end]
print("The email has been sent through " + mailserver)
print("It was sent on " + date_time)