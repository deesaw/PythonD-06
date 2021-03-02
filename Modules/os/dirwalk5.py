#program to find the files which has created 2 days 
import os,time
age=2*24*60*60
fpath1='C:/Users/admin/Desktop/PythonTutorials'
for (dirname, subdir, files) in os.walk(fpath1):
        for myfile in files:
                if myfile.endswith('.txt'):
                        filename=os.path.join(dirname,myfile)
                        fileage=time.time() - os.stat(filename).st_ctime 
                        if fileage < age:
                                        print(filename)

'''1 day =
24 hours/day × 60 minutes/hour × 60 seconds/minute = 86400 seconds/day
'''
'''current=time.time()
for (dirname,subdir,files) in os.walk(path):
    for file in files:
        fname=os.path.join(dirname,file)
        ctime=os.stat(fname).st_ctime   # seconds passed
        
        hrs=(current-ctime)/3600        # convert into hours passed
        
        if hrs <= 48:                    # if within last 48 hours
            print (fname)'''
