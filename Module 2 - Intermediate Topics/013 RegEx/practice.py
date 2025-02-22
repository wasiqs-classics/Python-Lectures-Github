import re

pattern = r"^p.....n$"
test_string = "python"
another_string = "pokemon"

result = re.match(pattern, another_string)

if result:
    print("Pattern found!")
else:
    print("Pattern not found.")

pattern1 = "^F...u?...e$"

pattern2 = "\d{2,5}"

if re.match(pattern2, "12345678"):
    print("Match found!")
else:
    print("Match not found!")


print(f"the message is {result}")


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

print(is_valid_email("wasiqonly@gmail.com"))  # Output: True