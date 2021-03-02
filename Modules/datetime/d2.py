#timedelta -- future and past dates can be caluclated
import datetime
bday=datetime.date(2000,7,26)
dt=datetime.timedelta(365)
print(bday+dt)
