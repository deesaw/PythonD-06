import datetime
bday=datetime.date(2000,7,26)
print(bday.strftime('%A, %B, %d, %Y'))
print("Ujwal was born on {: %A, %B, %d, %Y}".format(bday))
#print(msg.format(bday))
