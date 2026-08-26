# 1. WAP TO CALCULATE AREA O A TRIANGLE USING HERON'S FORMULA.

# a = float(input("Enter the 1st side of a triangle : "))
# b = float(input("Enter the 2nd side of a triangle : "))
# c = float(input("Enter the 3rd side of a triangle : "))
# print(a,b,c)
# s = (a + b + c)/2
# print(s)
# area = (s*(s-a)*(s-b)*(s-c))**0.5
# print("Area = " + str(area))


#2. WAP TO CALCULATE THE TOTAL NUMBER OF MONEY IN THE PIGGYBANK, GIVEN THE COINS OF RS 10, RS 5, RS 2 AND RE 1

# coins_of_10 = int(input("Enter the number of 10 Rs coins : "))
# coins_of_5 = int(input("Enter the number of 5 Rs coins : "))
# coins_of_2 = int(input("Enter the number of 2 Rs coins : "))
# coins_of_1 = int(input("Enter the number of 1 Re coins : "))
# total_amt = coins_of_10*10 + coins_of_5*5 + coins_of_2*2 + coins_of_1*1
# print("Total Amount in the PiggyBank : ", total_amt)

# 3. WAP TO PREPARE A GROCERY BILL. FOR THAT ENTER NAME OF THE ITEMS PURCHASED, QUANTITY IN WHICH IT IS PURCHASES, AND ITS PRICE PER UNIT. THEN DISPLAY ITEM QUANTITY, PRICE AMOUNT, TOTAL AMOUNT TO BE PAID.

# qty = float(input("Enter Number of quantity of item sold : "))
# value = float(input("Enter Price per Unit : "))
# discount = float(input("Enter the discount percentage : "))

# amt = qty * value
# tax = float(input("Enter the tax percentage : "))
# discount_amt = (amt*discount)/100
# sub_total = amt - discount_amt
# tax_amt = (sub_total*tax)/100
# total_amt = sub_total + tax_amt

# print("***************BILL***************")
# print("Quantity Sold : \t ", qty)
# print("Price per Item : \t ", value)
# print("\t \t -----------------------")
# print("Amount : \t\t", amt)
# print("Discount : \t\t-", discount_amt)
# print("   \t    \t -----------------------")
# print("Discounted Total : \t", sub_total)
# print("Tax : \t\t\t  +",tax_amt)
# print("    \t   \t -----------------------")
# print("Total amount to be Paid :  ", total_amt)

#4. WAP THAT PROMPTS USER TO ENTER HIS FIRST NAME AND LAST NAME AND THEN DISPLAYS A MESSAGE "GREETINGS!!! FIRST NAME LAST NAME"

# a = input("Enter your First Name : ")
# b = input("Enter Your Last Name : ")
# print("Greetings!!! " + a + " " + b)

# 5. WAP TO CALCULATE SALARY OF AN EMPLOYEE GIVEN HIS BASIC PAY, HRA = 10% OF BASIC PAY, TA = 5% OF BASIC PAY(ALL ENTERED BY USER). CALCULATE THE SALARY OF THE EMPLOYEE.

# basic_pay = float(input("Enter your Basic Pay : "))
# hra = float(input("Enter Percentage for your HRA : "))
# ta = float(input("Enter Percentage for your TA : "))
# salary = basic_pay + (basic_pay*hra)/100 + (basic_pay*ta)/100
# print("Your Salary : ", salary)

#6. WAP TO PROGRAM TO PRINT THE ASCII VALUE OF A CHARACTER.

# a = input("Enter a Character : ")
# b = ord(a)                                        #TYPE CONVERSION
# print(b)

#7. WAP TO CALCULATE A STUDENT'S RESULT BASED ON TWO EXAMINATIONS, 1 SPORTS EVENT, AND 3 ACTIVITIES CONDUCTED. THE WEIGHTAGE OF ACTIVITIES = 30 PERCENT, SPORTS = 20 PERCENT, AND EXAMINATION = 50 PERCENT.

# act = 30.0
# sports = 20.0
# exams = 50.0
# exams_total = 200.0
# acts_total = 60.0
# sports_total = 50.0

# print("***************INPUT MARKS***************")
# exam_1 = float(input("Enter marks in 1st exam out of 100 : "))
# exam_2 = float(input("Enter marks in 2nd exam out of 100 : "))
# sports_1 = float(input("Enter marks in sports activities out of 50 : "))
# act_1 = float(input("Enter marks in 1st activity out of 20 : "))
# act_2 = float(input("Enter marks in 2nd activity out of 20 : "))
# act_3 = float(input("Enter marks in 3rd activity out of 20 : "))

# exams_overall = exam_1 + exam_2
# acts_overall = act_1 + act_2 + act_3
# exams_percent = float(exams_overall * exams / exams_total)
# sports_percent = float(sports_1 * sports / sports_total)
# acts_percent = float(acts_overall * act / acts_total)
# total_percent = exams_percent + sports_percent + acts_percent

# print("***************RESULTS***************")
# print("Total Percent in Examination : ", exams_percent)
# print("Total Percent in Activities : ", acts_percent)
# print("Total Percent in Sports : ", sports_percent)
# print("*********************************")
# print("Total Percentage : ", total_percent)

#8. WAP TO PRINT THE DIGIT AT ONE'S PLACE OF A NUMBER.

# num = int(input("Enter any number : "))
# digit_at_ones_place = num%10
# print ("The digit at ones place of "+str(num)+" is "+str(digit_at_ones_place))

# 9. MOMENTUM IS CALCULATED AS, E=MC^2, WHERE M = MASS AND C = VELOCITY. WRITE A PROGRAM, THAT ACCEPTS AN OBJECT'S MASS AND VELOCITY AND DISPLAYS ITS MOMENTUM.

# mass = float(input("Enter Mass of the Object : "))
# velocity = float(input("Enter Velocity : "))
# momentum = mass * velocity*velocity
# print("Momentum : ", momentum)
