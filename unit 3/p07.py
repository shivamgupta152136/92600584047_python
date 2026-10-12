import shutil
import os

with open("source.txt", "w") as file:
    file.write("Hello Python")

shutil.copy("source.txt", "copy.txt")
print("File Copied Successfully")

shutil.move("copy.txt", "moved.txt")
print("File Moved Successfully")

os.remove("moved.txt")
print("File Deleted Successfully")