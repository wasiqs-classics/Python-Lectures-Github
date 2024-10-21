![Python Data Types](https://media.licdn.com/dms/image/D4D12AQFXNiOa46y5Cw/article-cover_image-shrink_720_1280/0/1702621289199?e=2147483647&v=beta&t=YJqsDKlXjyXLDr5npaJtac-L_LDiKXsM8H6KgLjOedU)
### 002: Variables and Data Types
In this lecture 002, we will learn about a very important and fundamental concept of variables and data types in details. 

#### Understanding Variables
A variable in programming is like a labeled box that holds information. Just as you might label a box "Books" and place some books inside, you can create a variable in Python and assign it a value. For example, you might have a variable named `age` that holds a number like `25`.

The general syntax of the variable is: variable_name = value

**Real-world Example**: 
Imagine you’re running a small library. You have different sections labeled "Science Fiction," "Mystery," and "Biographies." Each section holds a certain number of books. In Python, these sections are like variables, and the number of books represents the values stored in them:
   ```python
   science_fiction_books = 20
   mystery_books = 15
   biographies_books = 10
   ```

#### How Variables Are Stored in Memory
When you create a variable in Python, it’s stored in the computer's memory. Think of memory as a large storage unit with many compartments, each having a unique address. Python stores the variable’s value at a memory address and keeps track of where that value is stored using the variable's name. 

You can find the memory address of a variable using the `id()` function:
   ```python
   age = 25
   print(id(age))  # This prints the memory address where the value 25 is stored
   ```

#### Rules for Naming a Variable
1. **Start with a Letter or Underscore**: A variable name must begin with a letter (a–z, A–Z) or an underscore (`_`).
2. **Can Contain Letters, Digits, and Underscores**: You can use letters, digits, and underscores in the name (e.g., `user_age`, `number1`).
3. **Case-Sensitive**: `age` and `Age` are considered different variables.
4. **Avoid Keywords**: You cannot use Python's reserved words like `class`, `def`, `if`, etc., as variable names.

#### Constants
A **constant** is a type of variable whose value should not change throughout the program. Python doesn't have a built-in constant feature, but by convention, variables meant to be constants are written in all uppercase letters:
   ```python
   PI = 3.14159
   GRAVITY = 9.8
   ```
While Python allows changing these values, sticking to the convention helps others understand that these values should remain unchanged.

---

### Data Types in Python
Not all the data that we deal in our life is same, similarly in any programming language there are different data types and each data type has its associated functionality and purpose. For example user name in your social media accounts has a data type of string where as your age can be a number. 
Python provides several built-in data types to represent different kinds of values. Here are some of the most commonly used ones:

1. **Integers (`int`)**: Whole numbers, positive or negative, without a decimal point.
   ```python
   age = 25
   year = 2024
   ```
   *Use case*: Counting items, tracking age or years, etc.

2. **Floating-Point Numbers (`float`)**: Numbers with a decimal point.
   ```python
   price = 19.99
   temperature = -5.2
   ```
   *Use case*: Representing prices, measurements, or any value that requires precision.

3. **Strings (`str`)**: Text data enclosed in quotes.
   ```python
   name = "Alice"
   greeting = 'Hello, World!'
   ```
   *Use case*: Storing names, messages, or any textual information.

4. **Booleans (`bool`)**: Represent true or false values.
   ```python
   is_logged_in = True
   is_admin = False
   ```
   *Use case*: Conditional checks, like whether a user is logged in or not.

5. **Lists (`list`)**: Ordered collections of items, which can hold mixed data types.
   ```python
   fruits = ["apple", "banana", "cherry"]
   numbers = [1, 2, 3, 4.5]
   ```
   *Use case*: Storing multiple values in a single variable, like items in a shopping cart.

6. **Dictionaries (`dict`)**: Key-value pairs, useful for storing related data.
   ```python
   student = {"name": "Alice", "age": 20, "grade": "A"}
   ```
   *Use case*: Storing structured data, like user information or configuration settings.

7. **Tuples (`tuple`)**: Ordered collections, like lists, but immutable.
   ```python
   coordinates = (10, 20)
   ```
   *Use case*: Representing fixed data, like coordinates or constant configurations.

8. **Sets (`set`)**: Unordered collections of unique items.
   ```python
   unique_numbers = {1, 2, 3, 4}
   ```
   *Use case*: Removing duplicates from a list or checking for membership.

**NOTE: Lists, Dictionaries, Tuples and Sets are called collectables, like variables with can store more than one values (like arrays in programming language) and there is a separate lecture on it, 007 Collectables**

---

### Finding the Type of a Variable
You can determine the data type of a variable using the `type()` function:
   ```python
   age = 25
   print(type(age))  # Output: <class 'int'>
   ```

### Type Conversion
Python allows you to convert one data type into another:
   ```python
   # Convert integer to string
   age = 25
   age_str = str(age)
   
   # Convert string to float
   price = "19.99"
   price_float = float(price)
   
   # Convert float to integer
   temperature = 36.6
   temperature_int = int(temperature)
   ```

### Type Hints
In recent versions of Python, **Type Hints** were introduced to indicate what type a variable should hold. This is especially useful in large projects where maintaining clear code is critical.
Type hints in Python are a way to indicate the expected data types of function arguments, return values, and variables. While Python is a dynamically typed language, type hints are used to improve code readability and help with static analysis tools, which can catch type-related bugs before runtime.

**What does it mean that Python is a Dynamic Typed Language?**
Dynamic typing means that variables can change types at runtime, which offers flexibility but can lead to runtime errors. 
For example consider this program:

   ```python
   age = "Thirty"
   age = 30
   ```
In the above example, there will be no error as python determines the type at run time. However, in larger projects with hundreds of thousands (even millions) of lines of code and many files, it offers great problems and unexpected behaviors in the program execusion to bring errors in the program. Which are really difficult to sort by the developers. In order to handle this, we use static Typing. 
Static typing, on the other hand, enforces type constraints at compile-time, making code more predictable and easier to debug, which is crucial for large projects. 
This means that the variable, functions must inform about the data types they will store or return. For example in Web Applications Development in these days, TypeScript, a superset of JavaScript, introduces static types to help developers catch errors early and manage large codebases more effectively. Similarly, **Python uses type hints to achieve some benefits of static typing**, improving code clarity and enabling better tool support while maintaining Python's dynamic nature. Both approaches aim to balance flexibility with safety, enhancing developer productivity and code reliability.

**Why Use Type Hints?**

*Readability:* Makes the code easier to understand by clearly showing what type of data is expected.

*Tool Support:* IDEs and code editors can provide better autocompletion and error checking.

*Maintenance:* Helps other developers (or future you) understand the intended use of variables and functions.

   ```python
   # This is how you declare the type of a variable
   age: int = 1

   # You don't need to initialize a variable to annotate it
   a: int  # Ok (no value at runtime until assigned)

   # Doing so can be useful in conditional branches
   child: bool
   if age < 18:
     child = True
   else:
     child = False
   ```
General Syntax: 
**variable_name: type = value**

   ```python
   def greet(name: str) -> str:
       return f"Hello, {name}"
   ```
**NOTE: There is a complete section on Type Hints in Module 2 and we will discover further there. However you can [check this link](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) for further understanding of the concept of Type Hints.**

---

### Exercise: Practice What You’ve Learned
1. Create a variable called `favorite_color` and assign it your favorite color as a string.
2. Write a program that converts an integer `100` to a float and prints it.
3. Create a list of your top 3 favorite fruits. Print the type of the list and its elements.
4. Define a dictionary with keys `name`, `age`, and `city` representing a person’s details.
5. Create a set of days of a week.
6. Write a function with type hints that takes two integers as input and returns their sum.

---

#### Conclusion
With a solid understanding of variables, data types, and type conversion, you now have the foundation to start writing more complex programs. In the next lesson, we’ll explore **Operators and Expressions**, where you'll learn how to manipulate data using arithmetic and logical operators. Let’s keep building on what you’ve learned!

---
[![Next Lecture](../../Previous.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%201%20-%20Basic%20Topics/001%20Python%20Fundamentals)       [![Next Lecture](../../Next.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%201%20-%20Basic%20Topics/003%20Operators)
