import os
import time
file="c:/users/tring/desktop/fidelity/marks.csv"

print(os.path.getsize(file))
print(time.ctime(os.path.getctime(file)))
print(time.ctime(os.path.getatime(file)))
print(time.ctime(os.path.getmtime(file)))
print(dir(os.path))
print(os.path.splitext(file))
print(os.path.isdir(file))
print(os.path.isfile(file))
print(os.path.exists(file))
