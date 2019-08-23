#run python command in command prompt before executing the below code 

import os

#to list all files in directory

 os.listdir() 

#to rename a single image

os.rename('./existingName.jpg','./newName.jpg')

#more than one images

root= 'address of folder containing images'

for i,file in enumertate(os.listdir(root)):
	if file.endswith('.jpg'):
		os.rename(root+file, root+f"{1+1}.jpg")
		print(f"Renaming{file}....")