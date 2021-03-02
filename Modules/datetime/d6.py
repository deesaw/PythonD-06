#convert string to date time object
#strptime class
import datetime
bday="20/11/2002"
bday_format=datetime.datetime.strptime(bday,"%d/%m/%Y")
print(bday_format)


