import datetime

 

# Create a date object for George Washington's birthday

WashingtonsBirthDay = datetime.date(1970, 6, 8)

 

# Print Washington's BirthDay

print("George Washington's birthday is {}".format(WashingtonsBirthDay))

 

# Get the proleptic Gregorian ordinal for George Washington's birthday

gregorianOrdinal = WashingtonsBirthDay.toordinal()

print("George Washington was born on {}th day if you count from 01/01/01".format(gregorianOrdinal))
