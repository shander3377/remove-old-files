import os
import shutil
import time
def main():
 path = input("Tell me path of the folder: ")
 days = float((input("Tell me days: ")))
 seconds = time.time() - (days * 24 * 60 * 60)
 if os.path.exists(path):
     data = os.walk(path)
     for rootFolder, folders, files in data:
         for folder in folders:
             folderPath = os.path.join(rootFolder, folder)
             if seconds >= get_age(folderPath):
                  removeFolder(path) 
                  deleted_folders_count +=1
         for file in files:
             filePath = os.path.join(rootFolder, file)
    
             if seconds >= get_age(filePath):
                removeFile(path) 
                deleted_files_count +=1
 else: 
    print("path not found")
    print("Total folders deleted: {deleted_folders_count}")
    print("Total files deleted: {deleted_files_count}")
def get_age(path):
    ctime=os.stat(path).st_ctime
    return ctime
def removeFile(path):
# removing the file
	if not os.remove(path):

		# success message
		print("{path} is removed successfully")

	else:

		# failure message
		print("Unable to delete the "+path)
def removeFolder(path):
    # removing the file
	if not os.remove(path):

		# success message
		print("{path} is removed successfully")

	else:

		# failure message
		print("Unable to delete the "+path)
if __name__ == '__main__':
	main()