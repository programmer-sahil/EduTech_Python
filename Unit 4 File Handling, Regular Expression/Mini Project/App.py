import re

with open("emails.txt", "r") as f:
    content = f.read()

emails = re.findall(r"\b[A-Za-z0-9._%+-]+[A-Za-z0-9.-]@+\.[A-Z|a-z]{2,}\b", content)

with open("found_emails.txt", "w") as f:
    for email in emails:
        f.write(email + "\n")
