# with open('file.txt', "r") as f:
#     for line in f:
#         print(line.strip())

# with open("file.txt", "r") as file:
#     lines = file.readlines()
#     print(lines)

# with open("file.txt", "w") as f:
#     f.write("Hello Jupyter\n")
#     f.write("How old are you?\n")
#     f.write("I am 1000 years old\n")
    

# with open("file.txt", "r") as file:
#     lines = file.readlines()
#     print(lines)

# with open("file.txt", "a") as f:
#     f.write("This is the newest line.\n")

# with open("file.txt", "r") as file:
#     lines = file.readlines()
#     print(lines)

with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)

for line in lines:
    if "Mango" in line:
        updated_line = line.replace("Mango","Cherry")
        lines.append(updated_line)
        lines.remove(line)




# with open("example.txt", "a") as f:
#     f.write(updated_line)

