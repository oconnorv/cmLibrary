import os
import hashlib

cmsDirectory = "C:\\Users\\joconnor\\Desktop\\cmstorycopy"

removed = 0

def removeDups():
	global removed
	hashes = set()
	for root, dirs, files in os.walk(cmsDirectory):
		for i in files:
			with open(os.path.join(root,i),"rb") as currentFile:
				data = currentFile.read()
				hrhash = hashlib.md5(data).hexdigest()
				if hrhash not in hashes:
					hashes.add(hrhash)
					print("keeping " + os.path.join(i))
					currentFile.close()
				else:
					currentFile.close()
					os.remove(os.path.join(root,i))
					removed = removed + 1
					print("removed " + os.path.join(i) + " " + str(removed))

removeDups()
print("removed " + str(removed) + " files")