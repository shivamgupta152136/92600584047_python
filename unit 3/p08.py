import re

text = "Python123"
pattern = r"Python"

result = re.match(pattern, text)

if result:
    print("Pattern Matched")
else:
    print("Pattern Not Matched")