
print("Original")
print("==========")

# Opening the file
with open("file.txt", "r") as my_file:
    # reading a file
    content = my_file.read()
    print(content)

with open("file.txt", "w") as file:
    file.write("This is the new content")
    
print("After update")
print("===========")

with open("file.txt", "r") as my_file:
    print(my_file.read())

with open("file.txt", "a") as file:
    file.write("\nAnother line added")

print("Appended")
print("===========")

with open("file.txt", "r") as my_file:
    print(my_file.read())


