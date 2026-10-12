import re

text = "Python is easy. Python is powerful."

print("Match:", re.match("Python", text).group())

print("Search:", re.search("easy", text).group())

print("Find All:", re.findall("Python", text))