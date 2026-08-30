# WAP TO PRINT THE CALENDAR OF ANY GIVEN YEAR

import calendar
y = int(input("Enter the year : "))
m = 1
print("YOUR CALENDAR : - ")
cal = calendar.TextCalendar(calendar.SUNDAY)       #AN INSTANCE OF TEXTCALENDAR CLASS IS CREATED AND CALENDAR. SUNDAY MEANS THAT YOU WANT TO STAR DISPLAYING THE CALENDAR FROM SUNDAY.
i = 1
while i <= 12:
    cal.prmonth(y,i)
    i = i+1                  #prmonth() is a function of the class that prints the calendar for given month and year
