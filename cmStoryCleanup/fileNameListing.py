import os

cmsDirectory = "C:\\Users\\joconnor\\Downloads\\cmstory"

cmsFiles = open("cmstoryfiles.csv", "w")
cmsFiles.write("File Name, File Size (kb), File Path\n")

def buildCSV():
	for root, dirs, files in os.walk(cmsDirectory):
		for i in files:
			cmsFiles.write(os.path.join(i) + "," + str(os.path.getsize(os.path.join(root, i))/1024) + "," + os.path.join(root) + "\n")
	cmsFiles.close()

buildCSV()

#	Get the file name
#	for root, dirs, files in os.walk(cmsDirectory):
#		for i in files:
#			print(os.path.join(i))
#
# Get the file size	
#	for root, dirs, files in os.walk(cmsDirectory):
#		for i in files:
#			print(os.path.getsize(os.path.join(root, i)))
#
#Get the file path
#	for root, dirs, files in os.walk(cmsDirectory):
#		for i in files:
#			print(os.path.join(root))