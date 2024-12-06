### Lecture 009: Functions in Python
![Python Functions Syntax](https://miro.medium.com/v2/resize:fit:1200/1*IdSHO7WNuqxofYvYMIkhew.png)

---

#### Introduction to Functions

Functions are reusable blocks of code designed to perform a specific task. They enhance modularity, readability, and reduce redundancy in programs. By using functions, programmers can:
- Organize code into logical sections.
- Simplify debugging and maintenance.
- Encourage code reuse across different parts of a program.

Suppose we want to create a program that runs an autonomous vehicle. So we can divide our program into different functions. 
Like:
 - A function to start the car
 - A function to stop the car
 - Separate functions to control accelerators, brakes, sterring wheel etc.

> Dividing a complex problem into smaller chunks makes our program easy to understand and reuse.

---

### Types of Functions in Python

1. **Built-in Functions**: Provided by Python (e.g., `print()`, `len()`, `sum()`).
2. **User-defined Functions**: Created by programmers to perform custom operations.

---

### Creating Functions in Python

![Python Functions Syntax](https://www.boardinfinity.com/blog/content/images/2023/02/Python-Function-1.png)

To create a function, use the `def` keyword followed by the function's name and parentheses containing optional parameters. The function body is indented and includes the logic you want to execute. The `return` statement sends a result back to the caller (optional). Functions can be reused, making code more modular and manageable.

**Syntax**:
```python
def function_name(parameters):
    """Docstring: Explains what the function does."""
    # Function body
    return result  # Optional
```

Let's consider this example. 

**Example**:
```python
def greet(name):
    """Greet a user by name."""
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
```
This function `greet` accepts a parameter name, which is used to personalize a greeting. The `return` statement outputs a formatted string `Hello, {name}!`. When `greet("Alice")` is called, the function replaces `{name}` with `"Alice"`, producing `"Hello, Alice!"`, which is printed.

NOTE: All the functions must be called to see them in action. 

### Calling a Function
To call a function, use the function name followed by parenthesis (which may include the arguments). In the example above, `greet("Alice")` is when we called the function. 
- We first define a function, this is where we write its code.
- Then we make use it. Its called calling a function.  

---

### Parameters in Functions

1. **Positional Parameters**:
In positional parameters, Parameters are matched based on their order in the function call.

   ```python
   def add(a, b):
       return a + b

   print(add(3, 5))  # Output: 8
   ```
 **Example:** `add(3, 5)` passes 3 to the first parameter and 5 to the second.

2. **Named Parameters**:
Parameters are specified by name, improving clarity.

```python
def calculate_price(item, price, discount=0):
    """Calculate the price after applying a discount."""
    final_price = price - (price * discount / 100)
    return f"The price of {item} after a {discount}% discount is ${final_price:.2f}"

# Calling with named parameters
print(calculate_price(item="Laptop", price=1000, discount=10))
print(calculate_price(price=500, item="Headphones", discount=5))
```
 - The parameters `item`, `price`, and `discount` are used with their names during the function call.
 - This approach ensures clarity, especially when there are multiple parameters or default values.

3. **Default Parameters**:
Parameters with default values used if no argument is provided.
   ```python
   def greet(name="Guest"):
       return f"Welcome, {name}!"

   print(greet())  # Output: Welcome, Guest!
   ```
 **Example**: def `greet(name="Guest")` sets name to `"Guest"` when no value is given.

4. **Arbitrary Arguments (`*args`)**:
  Allows functions to accept any number of positional arguments, grouped as a tuple.
   ```python
   def display(*args):
       for arg in args:
           print(arg)

   display("Alice", "Bob", "Charlie")
   ```
    **Example:** `def sum_all(*args)` lets you sum any number of numbers. *Can you make the function?* 

5. **Arbitrary Keyword Arguments (`**kwargs`)**:
Accepts any number of named arguments as a dictionary.
   ```python
   def info(**kwargs):
       for key, value in kwargs.items():
           print(f"{key}: {value}")

   info(name="Alice", age=25, city="New York")
   ```
**Example:** def info(**kwargs) can handle inputs like info(name="Alice", age=25).

---

### Returning Values in Functions
Functions in python may and may not return values. 

A function can perform actions, print outputs, or modify data without returning a value. However, when a function does return something, it sends the result back to the caller.

**Example**: 
```python
def greet_user(name):
    """Greet a user with their name."""
    print(f"Hello, {name}!")

greet_user("Alice")  # Outputs: Hello, Alice!
```

Functions can return a single value or multiple values.

**Single Value**:
```python
def square(num):
    return num ** 2

print(square(4))  # Output: 16
```

**Multiple Values**:
When a function returns multiple values in Python, the return type is a `tuple` by default. For example: 

```python
def stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

print(stats([1, 2, 3]))  # Output: (1, 3, 6)
```
You can explicitly define the return type based on your preference, such as a list, dictionary, or any other object. For example:
```python
def get_numbers():
    return [1, 2, 3]

print(get_numbers())  # Output: [1, 2, 3]
```
Or return a dictionary 
```python
def get_user():
    return {"name": "Alice", "age": 25, "email": "alice@example.com"}

print(get_user())  # Output: {'name': 'Alice', 'age': 25, 'email': 'alice@example.com'}
```
Python's flexibility allows functions to return any data type you prefer, whether built-in types like lists and dictionaries or custom objects.

---

### Functions with Collections

You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

E.g. if you send a List as an argument, it will still be a List when it reaches the function:

**Working with Lists**:
```python
def double_list(lst):
    return [x * 2 for x in lst]

print(double_list([1, 2, 3]))  # Output: [2, 4, 6]
```

**Working with Dictionaries**:
```python
def update_dict(d, key, value):
    d[key] = value
    return d

print(update_dict({}, "name", "Alice"))  # Output: {'name': 'Alice'}
```

---

### Anonymous Functions (Lambda)

In Python, a lambda function is a special type of function without the function name. A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.

Syntax:
We use the lambda keyword instead of def to create a lambda function. Here's the syntax to declare the lambda function.
> lambda argument(s) : expression

Lambda functions are concise, single-expression functions.

**Example**:
```python
square = lambda x: x ** 2
print(square(5))  # Output: 25
```

Lambda functions can take any number of arguments:

```python
x = lambda a, b : a * b
print(x(5, 6))
```
or
```python
# lambda that accepts one argument
greet_user = lambda name : print('Hey there,', name)

# lambda call
greet_user('Delilah')

# Output: Hey there, Delilah
```
In the above example, we have assigned a lambda function to the greet_user variable. 
Here, name after the lambda keyword specifies that the lambda function accepts the argument named name.

**Use Case in Sorting**:
```python
data = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [('Bob', 20), ('Alice', 25), ('Charlie', 30)]
```
### Explanation
This example demonstrates sorting a list of tuples based on a specific key using Python's `sorted()` function.

1. **Input Data**:  
   `data` is a list of tuples where each tuple contains a name and an age:  
   `[("Alice", 25), ("Bob", 20), ("Charlie", 30)]`.

2. **Sorting Logic**:  
   The `sorted()` function is used to sort the list. The `key` argument specifies a function that determines the sort order.  
   Here, `lambda x: x[1]` is an anonymous function that takes a tuple `x` and returns its second element (age).

3. **Output**:  
   The tuples are sorted by age:  
   `sorted_data = [('Bob', 20), ('Alice', 25), ('Charlie', 30)]`.

---

### Recursive Functions

A recursive function calls itself to solve problems in smaller steps.
In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

The following image shows the working of a recursive function called recurse.
![Python recursive function](https://www.programiz.com/sites/tutorial2program/files/python-recursion-function.png)

Creating a recursive function requires careful planning to ensure it executes correctly and avoids infinite recursion. Below are the key considerations and steps:

### 1. **Define the Problem**
   - Understand how the problem can be broken into smaller subproblems of the same type.
   - Ensure the smaller subproblems eventually reach a trivial state.

### 2. **Base Case**
   - **Purpose**: Prevent infinite recursion by defining a stopping point.  
   - **Example**: In a factorial calculation, when `n == 0`, the recursion stops:
     ```python
     if n == 0:
         return 1
     ```

### 3. **Recursive Case**
   - Define how the function will call itself with a smaller or simpler input.
   - Ensure the inputs progress toward the base case to terminate recursion.

### 4. **Combine Results**
   - If recursion generates partial results, combine them to get the final output.
   - Example in summing elements: Combine the result of the smaller subproblem with the current element.

### 5. **Verify Termination**
   - Ensure all recursive paths eventually reach the base case. Failing this may lead to infinite recursion and a stack overflow.

## Examples

**Factorial**:
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```
1. **Base Case**: `n == 0`, returns `1`.
2. **Recursive Case**: Multiplies `n` by `factorial(n - 1)`.

### Example: Sum of a List
```python
def sum_list(nums):
    # Base Case
    if not nums:
        return 0
    # Recursive Case
    return nums[0] + sum_list(nums[1:])

print(sum_list([1, 2, 3, 4]))  # Output: 10
```

1. **Base Case**: If the list is empty, return `0`.
2. **Recursive Case**: Add the first element to the sum of the rest of the list.

**Fibonacci Sequence**:
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8
```
**Can you** find the base case ad recursive case in the above example?

Recursive functions, when used thoughtfully, are powerful for tasks like traversing trees, solving divide-and-conquer problems, and performing repetitive calculations.

---

### Pass by Value or Reference

Python passes **references to objects** (mutable objects like lists can be modified inside functions, but immutable ones like integers cannot).

**Example**:
```python
def modify_list(lst):
    lst.append(4)

numbers = [1, 2, 3]
modify_list(numbers)
print(numbers)  # Output: [1, 2, 3, 4]
```

---

### Nested Functions

A function can be defined inside another function.

**Example**:
```python
def outer_function():
    def inner_function():
        return "Hello from inner!"
    return inner_function()

print(outer_function())  # Output: Hello from inner!
```

---

### Real-World Example: ATM Machine

**ATM Program**:
```python
def atm():
    balance = 1000
    
    def check_balance():
        print(f"Your balance is: ${balance}")
    
    def deposit(amount):
        nonlocal balance
        balance += amount
        print(f"${amount} deposited successfully.")
    
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print(f"${amount} withdrawn successfully.")
    
    try:
        while True:
            print("\n1: Check Balance\n2: Deposit\n3: Withdraw\n4: Exit")
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                check_balance()
            elif choice == 2:
                amt = float(input("Enter deposit amount: "))
                deposit(amt)
            elif choice == 3:
                amt = float(input("Enter withdrawal amount: "))
                withdraw(amt)
            elif choice == 4:
                print("Thank you for using our ATM!")
                break
            else:
                print("Invalid choice!")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

atm()
```

---

### Exercise

1. Write a function that takes a list of numbers and returns the square of each number.
2. Create a function to count vowels in a given string.
3. Implement a recursive function to calculate the sum of the first `n` natural numbers.
4. Define a function that accepts `*args` and returns their sum.
5. Write a function to generate Fibonacci numbers up to a given number.

### Additional Exercises
Here are additional practice questions for functions in Python:

1. **Prime Checker**: Write a function that checks if a given number is prime and returns `True` or `False`.

2. **Palindrome Checker**: Create a function that determines if a string is a palindrome.

3. **Find Maximum**: Implement a function that takes a list of numbers and returns the largest number without using Python's built-in `max()` function.

4. **Custom Greeting**: Define a function that accepts a name and a time of day (morning, afternoon, evening) and returns a customized greeting.

5. **Temperature Converter**: Write a function that converts temperatures between Celsius and Fahrenheit.

6. **Word Frequency**: Create a function that takes a string and returns a dictionary with the frequency of each word in the string.

7. **Factorial with Default Parameters**: Write a function that calculates the factorial of a number. If no number is provided, it should default to 5.

8. **Reverse List**: Define a function that reverses a list without using built-in reverse methods.

9. **Unique Elements**: Write a function that takes a list and returns a new list containing only unique elements.

10. **Count Characters**: Implement a function that counts the number of each character in a string and returns the result as a dictionary.

These questions will help reinforce concepts like recursion, default parameters, and working with different data types. Try! 

---

### Conclusion

Functions are the backbone of Python programming, enabling modularity, readability, and reusability. Mastering functions opens the door to solving complex problems efficiently. With this knowledge, you’re now ready to explore **Modules**, the next step in your Python journey. Happy coding!

In the next lecture, we’ll dive into **Functions**, where you’ll learn to read from and write to files programmatically. Good luck, and happy debugging!

[![Prev Lecture](../../Previous.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%202%20-%20Intermediate%20Topics/008%20Debugging)       [![Next Lecture](../../Next.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%202%20-%20Intermediate%20Topics/010%20Modules)
