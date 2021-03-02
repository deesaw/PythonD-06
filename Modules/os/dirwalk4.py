import os
extns=["mp3","jpg","jpeg","mpg","mpeg"]
size=1 * 1024 * 1024
for (dirname, subdir, files) in os.walk('c:\\'):
	for myfile in files:
		filename=os.path.join(dirname,myfile)
		extn = os.path.splitext(filename)[-1]
		if extn in extns:
			if os.path.getfilesize(filename) > size:
				print(filename)
		
		