import os,time
cd=os.stat("C:\\Users\\admin\\Desktop\\PythonTutorials\\dirwalk\\dirwalk1.py").st_ctime
print(time.strftime('%Y%m%d',time.gmtime(cd)))

