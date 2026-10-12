import re

with open("data.txt", "w") as file:
    file.write("Contact: abc@gmail.com")
    file.write("\nEmail: student@gmail.com")

with open("data.txt", "r") as file:
    text = file.read()

emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)

print("Email Addresses Found:")
for email in emails:
    print(email)