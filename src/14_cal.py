"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime
from datetime import date

c = calendar.TextCalendar(calendar.SUNDAY)
now = datetime.now()
str = c.formatmonth(now.year, now.month)

year_month = input("month and year: 00/0000 format")

try:
  if (len(year_month) == 0):
    str = c.formatmonth(now.year, now.month)
    print(str)
  elif '/' in year_month:
    new_date = year_month.split('/')
    # print(new_date)
    str = c.formatmonth(int(new_date[1]), int(new_date[0]))
    print(str)
  elif '/' not in year_month:
    str = c.formatmonth(now.year, int(year_month))
    print(str)
except:
  print('wrong format')