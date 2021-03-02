'''Write a program to display the calendar of the given year and month
Note: 
1. import calendar and sys
2. Send values as args
3. if values are not sent as args take input from users'''


import calendar
import sys

if len(sys.argv) == 3:
    mm=int(sys.argv[2])
    y=len(sys.argv[1])
    yy=int(sys.argv[1])
 
    if ((y<4) or (mm>12)):        
        print("Please pass four digit year and month should not be greater than 12")
    else:
        print(calendar.month(yy,mm))
else:
    yy=int(input("Enter 4 digit year:"))
    mm=int(input("Enter month less than 13  :"))
    print(calendar.month(yy,mm))
        
    
