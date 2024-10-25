![Python Strings](https://www.techprofree.com/wp-content/uploads/2024/04/Introduction-to-Python-Strings.jpg)

### 006: Strings and Numbers in Python

#### Introduction

In this lecture, we’ll explore **strings** and **numbers**, two of the most fundamental data types in Python. Strings are sequences of characters, while numbers can be integers, floating-point values, or even complex numbers. By understanding these data types and how to manipulate them, you can build more dynamic and flexible programs.

---

### Strings

A **string** in Python is a sequence of characters enclosed in single (`'`) or double quotes (`"`). They are widely used for handling text in Python.

**Example**:
```python
greeting = "Hello, World!"
```

#### Strings as Arrays

Strings in Python behave like arrays of characters. Each character can be accessed using its index.

**Example**:
```python
first_letter = greeting[0]
print(first_letter)  # Output: H
```

#### Looping Through Strings

You can iterate over each character in a string using a `for` loop.

**Example**:
```python
for char in greeting:
    print(char)
```

#### Checking Substrings

To check if a certain substring exists within a string, use the `in` keyword.

**Example**:
```python
print("World" in greeting)  # Output: True
```

#### String Slicing

Slicing allows you to extract parts of a string by specifying a start and end index.

**Example**:
```python
substring = greeting[0:5]
print(substring)  # Output: Hello
```

#### Modifying Strings

Although strings in Python are immutable, you can create new strings based on modifications.

- **Lowercase/Uppercase**:
```python
print(greeting.lower())  # Output: hello, world!
print(greeting.upper())  # Output: HELLO, WORLD!
```

- **Removing Whitespaces**:
```python
trimmed_string = "   Hello!   ".strip()
print(trimmed_string)  # Output: Hello!
```

- **Replacing Parts of a String**:
```python
new_greeting = greeting.replace("World", "Python")
print(new_greeting)  # Output: Hello, Python!
```

- **Splitting Strings**:
You can split a string into a list based on a delimiter (default is space).

**Example**:
```python
words = greeting.split()
print(words)  # Output: ['Hello,', 'World!']
```

#### Concatenating Strings

You can combine strings using the `+` operator.

**Example**:
```python
full_greeting = "Hello" + " " + "Python"
print(full_greeting)  # Output: Hello Python
```

#### String Formatting

Use `format()` or **f-strings** for more dynamic string formatting.

**Example**:
```python
name = "Alice"
formatted_string = f"Hello, {name}!"
print(formatted_string)  # Output: Hello, Alice!
```

#### Escape Characters

Escape characters allow you to insert special characters within a string (like newlines or quotation marks).

**Example**:
```python
escaped_string = "She said, \"Hello!\""
print(escaped_string)  # Output: She said, "Hello!"
```

---
## Important String Methods

**count()**
--------
**Description:** Returns the number of non-overlapping occurrences of a substring in a string.

**Example:**
```python
    text = "hello world"
    count = text.count("l")
    print(count)  # Outputs: 3
```
**Use Case:** Useful for counting specific characters or substrings in a larger string, like counting word frequencies in text analysis.

**encode()**
--------
**Description:** Encodes the string using the specified encoding. By default, it’s UTF-8.

**Example:**
```python
    text = "hello"
    encoded_text = text.encode()
    print(encoded_text)  # Outputs: b'hello'
```
**Use Case:** Often used in preparing text data for transmission over the internet or storage in binary files.

**decode()**
--------
**Description:** Decodes the encoded string back to a regular string.

**Example:**
```python
    encoded_text = b'hello'
    decoded_text = encoded_text.decode()
    print(decoded_text)  # Outputs: hello
```
**Use Case:** Useful when receiving or reading encoded data that needs to be transformed back into a string.

**find()**
--------
**Description:** Returns the lowest index in the string where the substring is found. Returns -1 if the substring is not found.

**Example:**
```python
    text = "hello world"
    index = text.find("world")
    print(index)  # Outputs: 6
```
**Use Case:** Useful for locating substrings within a string. Unlike `index()`, it doesn’t raise an error if the substring is not found.

**index()**
--------
**Description:** Similar to `find()`, but raises a `ValueError` if the substring is not found.

**Example:**
```python
    text = "hello world"
    index = text.index("world")
    print(index)  # Outputs: 6
    # text.index("mars") would raise a ValueError
```
**Use Case:** Use it when you expect the substring to be found and want to handle the error explicitly if it's not.

**rfind()**
--------
**Description:** Returns the highest index in the string where the substring is found. Returns -1 if the substring is not found.

**Example:**
```python
    text = "hello hello"
    index = text.rfind("hello")
    print(index)  # Outputs: 6
```
**Use Case:** Useful for finding the last occurrence of a substring.

**rindex()**
--------
**Description:** Similar to `rfind()`, but raises a `ValueError` if the substring is not found.

**Example:**
```python
    text = "hello hello"
    index = text.rindex("hello")
    print(index)  # Outputs: 6
    # text.rindex("mars") would raise a ValueError
```
**Use Case:** Use it when you expect the substring to be found and want to handle the error explicitly if it's not.

**More String Methods**: [Python String Methods on W3schools](https://www.w3schools.com/python/python_strings_methods.asp)

---

### Numbers

In Python, there are three types of numbers: **integers**, **floats**, and **complex numbers**.

#### Integer

An integer is a whole number, positive or negative, without decimals.

**Example**:
```python
num = 10
```

#### Float

A float is a number with a decimal point.

**Example**:
```python
pi = 3.14159
```

#### Complex Numbers

Complex numbers have a real part and an imaginary part, represented as `a + bj`.

**Example**:
```python
complex_num = 2 + 3j
```

---

### Random Numbers

Python's `random` module allows you to generate random numbers, which can be useful in various applications like games, simulations, or generating random test data.

#### Generating Random Numbers

- **`random.randint()`**: Generates a random integer within a range.
  
  **Example**:
  ```python
  import random
  random_num = random.randint(1, 10)
  print(random_num)
  ```

- **`random.random()`**: Generates a random float between 0 and 1.
  
  **Example**:
  ```python
  random_float = random.random()
  print(random_float)
  ```

#### Shuffling Lists

You can shuffle a list randomly using `random.shuffle()`.

**Example**:
```python
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # Output: [4, 1, 5, 3, 2] (example)
```

---

**More on Random Numbers**: [Python Random Module](https://www.w3schools.com/python/module_random.asp)

---

### Exercise

1. Write a Python program to check if the word "Python" is present in a given string.
2. Create a program that generates a random number between 1 and 100.
3. Convert a string to uppercase and remove any whitespaces from both ends.
4. Write a program that takes a user's name as input and prints a greeting using string formatting.
5. Generate a list of 5 random integers between 1 and 50 and print them in ascending order.

---

### Conclusion

In this lesson, we explored **strings** and **numbers**, two foundational data types in Python. Understanding how to manipulate text and numbers is essential for most programs, and we’ve learned the basics of string operations, number types, and random number generation. With these skills, you’re well-prepared to move forward into more complex topics like **Functions**, which will be covered in the next lesson. Keep practicing!

[![Next Lecture](../../Previous.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%201%20-%20Basic%20Topics/005%20Loops)       [![Next Lecture](../../Next.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%201%20-%20Basic%20Topics/007%20Collectables)
