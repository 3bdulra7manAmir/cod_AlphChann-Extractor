import os
import time
from PIL import Image

dirPath = input("Enter The Path Please: ")  # Get all files inside this directory
dirList = os.listdir(dirPath)
# print(dirList)  # prints all files # Just for Debugging

x = 0
z = 0
for file in os.listdir(dirPath):
    try:
        if ("spc" in file) or ("sp" in file):  # why "spc"?... because usually cos is located in the tga images with spc or just sp in it's naming
            img = Image.open(f"{dirPath}/{file}")
            r, g, b, a = img.split()
            a.save(f"{file.split('.')[0]}.tga")
        x += 1
    except ValueError:
        z = 1
        print(f"Image {file} doesn't have Alpha channel")

if z != 1:
    print("Extraction Completed")
    time.sleep(2)
