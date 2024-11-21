mystring = "Hello World" #11 characters

for char in mystring:
    print(char)

string1 = "Cat eats rat"

print("ats" in string1) 

# string slicing

string2 = "RED GREEN BLUE"
substring1 = string2[0:3]
print(substring1)

substring2 = string2[4:9]
print(substring2)

# Methods in string

print(len(string1))

check_Str = "Hello I am learnig Python Basics"
starting = int(len(check_Str)/2)
print(starting)
substring3 = check_Str[starting:starting+5]
print(substring3)

msg = "Hi hOw ArE yOu?"
print(msg.lower())
print(msg.upper())

msg1 = "   This is a Text     "
print(msg1)
print(msg1.strip()) #strip removes whitespaces. 

message = "Hello Rayan how you doing?"
print(message.replace("Rayan", "Wasiq"))

new_message = "WTF wrong with you?"
filtered_message = new_message.replace("WTF", "What is")
print(filtered_message)

sentence = "The weather is too good today"
split_sentence = sentence.split(' ') # this method converts a string into list
print(split_sentence)

data="Wasiq,0232331,email@gmal.co,male"
user_data = data.split(',')
print(user_data)
user_name = user_data[0]
print(user_name)

msg3 = "Hello"
msg4 = "World"

msg5 = msg3 + " " + msg4 #concatenation - combining strings
print(msg5)

name = "Wasiq"
age = 37

print(f"Hello {name} \t you are {age} years young!")

msgs = "She said: \"She was hungry\""
print(msgs)

mymsg = "There were 23 members and they all were male."
print(mymsg.count("e"))

passs = "letmein123"
encoded_pass = passs.encode()
print(encoded_pass)
decoded_text = encoded_pass.decode()
print(decoded_text)

word = mymsg.find("were") # it finds the index of the word we are looking for. 
print(word)

word1 = mymsg.rfind("were")
print(word1)

number = 4 + 7j

import random

random_num = random.randint(1,10)
print(random_num)

print(random.random())

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # Output: [4, 1, 5, 3, 2] (example)