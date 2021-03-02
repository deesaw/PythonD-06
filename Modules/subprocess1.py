import subprocess
#on windows

print(subprocess.run(['dir'], shell=True)


#checking the output

output = subprocess.check_output(['dir'],shell=True)
print ('Have %d bytes in output' % len(output))
print (output)


#hide output get status
success=subprocess.run("ping www.google.com",stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print(success.returncode)









