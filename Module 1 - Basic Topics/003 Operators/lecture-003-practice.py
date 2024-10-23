# Operators

# Arithematic Operators

a = 10
b = 20

result = a + b

result1 = a - b

divide = 22/7
print(divide)

divide_new = 6 // 5 # floor division converts the division into integer values. 
print(divide_new)

# % modulus provides the remainder. 

output = 4 % 3 
print(output)


squared = 4 ** 3 # 4 x 4 x 4
print(squared)

# Comparison Operators

print(a != b)
print(a > b)

# Logical Operators

# and, or, not

admin = "Pak123"
password = "system"
age = 50

print(admin == "Pak123" and password == "system" and not age == 40)

c = 50 # assignment operator
c += 5 # c = c + 5, addition assignment operator
print(c)

x = [1, 2, 3]
y = x
print(x is y)  # Output: False

k = 10
print(type(k) is int) # we can use it to check the type of a variable as well. 

restricted_word = "Dafa"

sentence = "tum yaha se dafa hojao"

print(restricted_word.lower() in sentence)

