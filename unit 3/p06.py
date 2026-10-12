import os
import sys

if not os.path.exists("MyFolder"):
    os.mkdir("MyFolder")

print("Directory Created")
print("Directory Exists:", os.path.exists("MyFolder"))

print("Current Directory:", os.getcwd())
print("Directory Contents:", os.listdir("."))

print("Python Version:", sys.version.split()[0])