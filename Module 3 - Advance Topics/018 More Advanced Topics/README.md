![Python Advance Concepts](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20210917204112/Top-10-Advance-Python-Concepts-That-You-Must-Know.png)

Below is a comprehensive lecture on **Advanced Topics in Python** that covers a range of powerful features to write efficient, elegant, and expressive code. We’ll walk through each topic, explain its purpose, show its syntax, provide multiple examples, and discuss practical use cases.

---

# Advanced Topics in Python

## 1. Comprehensions

### **What are Comprehensions?**  
Comprehensions provide a concise way to create collections (lists, dictionaries, sets, or generators) from iterables. They allow you to transform, filter, and combine data in a single, readable expression.

### **Benefits:**  
- **Concise and Readable:** Reduces boilerplate loops.  
- **Expressive:** Combines mapping and filtering in one line.

### **Syntax & Examples:**

#### **General Syntax for List Comprehensions**

```python
[ expression for item in iterable if condition ]
```

For nested comprehensions, you can add additional `for` clauses:

```python
[ expression for item1 in iterable1 for item2 in iterable2 if condition ]
```

---

#### **List Comprehension**
```python
# Create a list of squares from 0 to 9
squares = [x ** 2 for x in range(10)]
print("Squares:", squares)
# Output: Squares: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

#### **Dictionary Comprehension**
```python
# Create a dictionary with numbers as keys and their squares as values
squares_dict = {x: x ** 2 for x in range(5)}
print("Squares Dict:", squares_dict)
# Output: Squares Dict: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

#### **Set Comprehension**
```python
# Create a set of even numbers from 0 to 9
evens = {x for x in range(10) if x % 2 == 0}
print("Evens:", evens)
# Output: Evens: {0, 2, 4, 6, 8}
```

#### **Generator Expression**
```python
# Create a generator for cubes of numbers from 0 to 4
cubes = (x ** 3 for x in range(5))
for cube in cubes:
    print(cube, end=" ")
# Output: 0 1 8 27 64
```

### **Practical Use Cases:**  
- Filtering and transforming data from lists or files.
- Quickly generating collections for further processing.
- Memory-efficient iteration with generator expressions.

### More Examples

Here are some more advanced examples for different applications of list comprehensions. 

### **Example 1: Nested List Comprehension with a Condition**

Suppose we have a matrix (a list of lists) and we want to flatten it while filtering out only the odd numbers:

```python
# Define a matrix (list of lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Flatten the matrix and select only odd numbers
flattened_odds = [num for row in matrix for num in row if num % 2 == 1]

print("Flattened Odds:", flattened_odds)
# Output: Flattened Odds: [1, 3, 5, 7, 9]
```

**Explanation:**  
- The outer loop iterates over each `row` in `matrix`.
- The inner loop iterates over each `num` in the `row`.
- The condition `if num % 2 == 1` filters out even numbers, keeping only odd ones.

---

### **Example 2: Nested Dictionary Comprehension with a Condition**

Imagine we want to create a dictionary where the keys are numbers (1 to 5) and the values are lists of their multiples up to 10× the key, but only include the even multiples.

```python
# Dictionary comprehension with nested list comprehension
multiples = {
    x: [y for y in range(x, x * 10 + 1, x) if y % 2 == 0]
    for x in range(1, 6)
}

print("Even Multiples Dictionary:", multiples)
# Possible Output:
# Even Multiples Dictionary: {1: [2, 4, 6, 8, 10], 2: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], ...}
```

**Explanation:**  
- The outer dictionary comprehension iterates over numbers `x` from 1 to 5.
- For each `x`, a list comprehension generates multiples of `x` (using `range(x, x * 10 + 1, x)`).
- The inner condition `if y % 2 == 0` ensures only even multiples are included in the list.

---

### **Example 3: Categorizing Names by Initial Letter**  
Suppose we have a list of names, and we want to group them by their starting letter.

```python
# List of names
names = ["Alice", "Arham", "Bilal", "Ayesha", "Babar", "Charlie", "Catherine", "Ali"]

# Dictionary comprehension to group names by first letter
name_groups = {letter: [name for name in names if name.startswith(letter)] for letter in "ABC"}

print(name_groups)
```

**Output:**
```python
{'A': ['Alice', 'Arham', 'Ayesha', 'Ali'], 'B': ['Bilal', 'Babar'], 'C': ['Charlie', 'Catherine']}
```

**Explanation:**
- The dictionary comprehension iterates over `"ABC"` (keys).
- The values are lists created using **list comprehension** that filters names based on their starting letter (`name.startswith(letter)`).

---

### **Example 4: Word Frequency Counter Using Dictionary Comprehension**  
We can count word occurrences in a given sentence.

```python
# Sample text
text = "apple banana apple cherry banana apple cherry cherry"

# Split text into words
words = text.split()

# Dictionary comprehension to count word frequency
word_count = {word: words.count(word) for word in set(words)}

print(word_count)
```

**Output:**
```python
{'banana': 2, 'apple': 3, 'cherry': 3}
```

**Explanation:**
- We create a **set** of words (to get unique words).
- We iterate over this set and count occurrences using `words.count(word)`.
- The dictionary comprehension stores words as keys and their counts as values.

---

### **Example 5: Creating a Dictionary from a List of Pairs**  
Suppose we have a list of tuples representing student names and their scores, and we want to convert it into a dictionary.

```python
# List of tuples (name, score)
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Alice", 90), ("Bob", 88)]

# Dictionary comprehension to store latest score of each student
student_scores = {name: score for name, score in students}

print(student_scores)
```

**Output:**
```python
{'Alice': 90, 'Bob': 88, 'Charlie': 78}
```

**Explanation:**
- The dictionary comprehension iterates over `(name, score)` tuples.
- Since dictionaries do not allow duplicate keys, the last encountered score for each student remains in the final dictionary.

---

### **Conclusion**
Dictionary comprehensions are powerful for **grouping, filtering, and transforming** text-based data efficiently. Whether it's categorizing names, counting words, or converting lists into structured data, they provide a concise and readable solution. 🚀

---

## 2. Understanding Decorators, Generators, Closures, and Higher-Order Functions in Python

These concepts enhance how you structure and reuse your code. 

To understand these **advanced Python concepts**, we will follow a structured order:  

1️⃣ **Higher-Order Functions** (Foundation for understanding Decorators and Closures)  
2️⃣ **Closures** (Key to understanding function behavior)  
3️⃣ **Decorators** (Built using Higher-Order Functions and Closures)  
4️⃣ **Generators** (An entirely different but related topic that makes iteration efficient) 

### **Higher-Order Functions**

#### **What Are They?**  
A **higher-order function** is a function that **takes another function as an argument** or **returns a function as a result**.

#### **Why Use Higher-Order Functions?**  
- Allows for **function composition** (combining multiple functions for reuse).  
- Helps in **functional programming** paradigms like `map()`, `filter()`, and `reduce()`.  
- Forms the foundation for **decorators**.

#### **Example 1: Passing a Function as an Argument**
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def process_function(func, name):
    return func(name)

print(process_function(greet, "Alice"))  # Output: Hello, Alice!
```

#### **Example 2: Similar Example with lambda functions**

```python
def apply_func(func, value):
    return func(value)

result = apply_func(lambda x: x ** 2, 5)
print("Square:", result)  # Output: Square: 25
```

#### **Example 3: Returning a Function**
```python
def multiplier(factor: int):
    def multiply(number: int) -> int:
        return number * factor
    return multiply

times3 = multiplier(3)
print(times3(5))  # Output: 15
```

#### **Practical Use Cases**
- Wrapping logic inside **reusable functions**.
- **Decorators** are built using higher-order functions.
- Used in **functional programming** with `map()`, `filter()`, and `reduce()`.


### **Closures**

#### **What Are They?**  
A closure is a feature in many programming languages, including Python, that allows a function to remember and access variables from an enclosing scope even after the outer function has finished executing.

In simpler terms, a closure is an inner function that has access to variables from its containing (or outer) function, even after that outer function has completed its execution. We can say, basically closure is a nested function that allows us to access variables of the outer function even after the outer function is closed.

To understand it better, let's (re)take a look at Python Nested Functions:

```python

def outer_scope():
    name = 'Wasiq'
    city = 'Karachi'

    def inner_scope():
        print(f"Hello {name}, Greetings from {city}")

    return inner_scope()

outer_scope()

```
In this example, the `outer_scope` function defines two local variables: `name` and `city`. It then defines and immediately calls `inner_scope`, which prints a greeting message using the `name` and `city` variables from the enclosing scope. 
When `outer_scope` is called, the nested function `inner_scope` runs, producing the greeting message: "Hello Wasiq, Greetings from Karachi".

Now, let's modify the example to return the inner function without executing it immediately:

```python

def outer_scope():
    name = 'Wasiq
    city = 'Karachi'

    def inner_scope():
        print(f"Hello {name}, Greetings from {city}")

    return inner_scope

# Assigning the inner function to a variable
greeting_func = outer_scope()

# Calling the inner function
greeting_func()

```

Here, `outer_scope` defines `name` and `city` as variables similarly to the above example. It then defines and returns the `inner_scope` function but this time without calling it (that is, `inner_scope` instead of `inner_scope()`),

When `greeting_func = outer_scope()` is executed, it assigns the `inner_scope` function returned by `outer_scope` to `greeting_func`.

Now, `greeting_func` holds a reference to the `inner_scope` function. Calling `greeting_func()` executes `inner_scope`, which prints: "Hello Wasiq, Greetings from Karachi".

Even though `outer_scope` has finished executing by the time we call `greeting_func()`, the `inner_scope` function (now referenced by `greeting_func`) retains access to the variables `name` and `city` from its enclosing scope. This is what makes it a closure – it "closes over" the variables from its containing scope. 

#### **More Examples:**

```python
def make_multiplier(factor: int):
    def multiplier(n: int) -> int:
        return n * factor
    return multiplier

times3 = make_multiplier(3)
print(times3(10))  # Output: 30
```

or consider this basic example:

```python

def fun1(x):
  
    # This is the outer function that takes an argument 'x'
    def fun2(y):
      
        # This is the inner function that takes an argument 'y'
        return x + y  # 'x' is captured from the outer function
    
    return fun2  # Returning the inner function as a closure

# Create a closure by calling outer_function
closure = fun1(10)

# Now, we can use the closure, which "remembers" the value of 'x' as 10
print(closure(5)) 

```
**Explanation**

- Outer Function (fun1): Takes an argument x and defines the fun2. The fun2 uses x and another argument y to perform a calculation.
- Inner Function (fun2): This function is returned by fun1 and is thus a closure. It “remembers” the value of x even after fun1has finished executing.
- Creating and Using the Closure: When you call fun1(10), it returns fun2 with x set to 10. The returned fun2(closure) is stored in the variable closure. When you call closure(5), it uses the remembered value of x (which is 10) and the passed argument y (which is 5), calculating the sum 10 + 5 = 15.

For more info: 
- [Check this article](https://www.freecodecamp.org/news/first-class-functions-and-closures-in-python/) on freecodecamp.org
- [Learn more about closures](https://www.geeksforgeeks.org/python-closures/)

#### **Practical Use Cases**
- **Data encapsulation** (similar to private variables in classes).  
- Used in **caching and memoization**.  
- **Building decorators** that need to maintain state.


### **Decorators**

#### **What Are They?**  
Decorators are functions that modify the behavior of other functions without permanently modifying them. They are useful for logging, access control, caching, and more.

#### **Syntax & Examples:**

```python
# A simple decorator that logs function calls
def decorator_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@decorator_function  # Decorator syntax
def base_function() -> None:
    print("Calling base function")

base_function()
```
*Comments:*  
- The `decorator_function` function wraps the `base_function` function to print details before and after its execution.

**Example of a Simple Decorator:**

```python

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

```

#### Need for Decorators
- **Code Reusability** : Instead of repeating the same logic in multiple functions, you can encapsulate it in a decorator and reuse it wherever needed.
- **Separation of Concerns** : Decorators allow you to separate cross-cutting concerns (e.g., logging, timing) from the core logic of your functions.
- **Cleaner Code** : By abstracting away repetitive code into decorators, your main functions remain concise and focused on their primary purpose.
- **Extensibility** : You can easily add or remove functionality by applying or removing decorators without modifying the original function.

#### **How Decorators Work?**

1. **Function Wrapping**: A decorator is essentially a higher-order function—a function that takes another function as input and returns a new function.
2. **Closure**: The inner function (`wrapper`) inside the decorator captures the original function and any additional arguments or logic. This is achieved using closures.
3. **Execution Flow**:
   - When you apply a decorator to a function, the original function is passed to the decorator.
   - The decorator modifies or extends the behavior of the function and returns a new function.
   - When the decorated function is called, the modified function (returned by the decorator) is executed instead of the original function.

##### Step-by-Step Execution:
```python
def my_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@my_decorator
def greet():
    print("Hello, World!")

# Equivalent to:
greet = my_decorator(greet)

greet()
```

1. The `greet` function is passed to `my_decorator`.
2. Inside `my_decorator`, the `wrapper` function is defined, which wraps the original `greet` function.
3. The `wrapper` function is returned and replaces the original `greet` function.
4. When `greet()` is called, the `wrapper` function is executed, adding extra behavior before and after calling the original `greet`.

#### **Use Cases of Decorators**

1. **Logging**: Track when and how functions are called.
2. **Authentication and Authorization**: Restrict access to certain functions based on user roles.
3. **Caching/Memoization**: Store results of expensive function calls to avoid redundant computations.
4. **Performance Measurement**: Measure the execution time of functions.
5. **Input Validation**: Validate inputs to functions before execution.
6. **Retry Mechanism**: Automatically retry failed function calls.
7. **Debugging**: Add debugging information to functions during development.

---
#### **Practical Examples**

##### 1. **Logging Decorator**
A decorator to log the execution of a function:
```python
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

print(add(3, 5))
```

**Output:**
```
Calling add with arguments (3, 5) and {}
add returned 8
8
```

##### 2. **Timing Decorator**
A decorator to measure the execution time of a function:
```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)

slow_function()
```

**Output:**
```
slow_function took 2.0023 seconds to execute
```

##### 3. **Access Control Decorator**
A decorator to restrict access to certain users:
```python
def admin_only(func):
    def wrapper(user, *args, **kwargs):
        if user != "admin":
            raise PermissionError("Only admins can access this function.")
        return func(user, *args, **kwargs)
    return wrapper

@admin_only
def sensitive_operation(user):
    print(f"{user} is performing a sensitive operation.")

sensitive_operation("admin")  # Works fine
sensitive_operation("guest")  # Raises PermissionError
```

##### 4. Memoization with Decorators
```python
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print(f"Fetching from cache for {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Calculates and caches results
print(fibonacci(10))  # Fetches from cache
```


### **4. Generators**  

#### **What Are Generators?**  
A **generator** is a special type of iterator that **yields values one at a time** instead of returning them all at once. It **saves memory** by generating values lazily.

#### **Why Use Generators?**  
- Efficient **memory usage** (useful for large datasets).  
- Works well with **infinite sequences**.  
- Used in **streaming data processing**.  

#### **Syntax: Using `yield` Instead of `return`**
```python
def countdown(n: int):
    while n > 0:
        yield n
        n -= 1

counter = countdown(5)
print(next(counter))  # Output: 5
print(next(counter))  # Output: 4
print(next(counter))  # Output: 3
```

#### **Example: Fibonacci Sequence Generator**
```python
def fibonacci(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Using the generator
for num in fibonacci(7):
    print(num, end=" ")
# Output: 0 1 1 2 3 5 8
```

#### **Practical Use Cases**
- **Processing large files line by line** (e.g., reading logs).  
- **Streaming data in real-time applications**.  
- **Generating infinite sequences without running out of memory**. 

### **Conclusion**

These four concepts **enhance Python's flexibility and efficiency**:

✅ **Higher-Order Functions** → Make code reusable.  
✅ **Closures** → Remember values even after function execution.  
✅ **Decorators** → Modify functions dynamically.  
✅ **Generators** → Handle large data efficiently.  

---

## **Sub Exercise**

1️⃣ **Create a function `power_function(exp)`**  
   - It should return a function that raises a number to the power `exp`.  
   - Use **closures**.  

2️⃣ **Create a decorator `@timeit`**  
   - It should calculate the execution time of any function it decorates.  

3️⃣ **Modify the Fibonacci generator**  
   - Add a feature where it only yields **even Fibonacci numbers**.  

4️⃣ **Write a generator `read_large_file(filename)`**  
   - It should read a large file **line by line**, without loading the entire file into memory.  

---


## 3. Map, Filter, and Reduce

These functional programming tools process iterables in a concise manner.

### **Map**

#### **What It Does:**  
Applies a function to every item in an iterable.

#### **Example:**

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared:", squared)
# Output: Squared: [1, 4, 9, 16, 25]
```

### **Filter**

#### **What It Does:**  
Filters items from an iterable for which a function returns True.

#### **Example:**

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)
# Output: Evens: [2, 4, 6]
```

### **Reduce**

#### **What It Does:**  
Applies a function cumulatively to the items of an iterable, reducing it to a single value. (Requires `functools.reduce`.)

#### **Example:**

```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda a, b: a * b, numbers)
print("Product:", product)
# Output: Product: 24
```

### **Practical Use Cases:**  
- **Map:** Transforming data (e.g., converting a list of strings to integers).
- **Filter:** Data validation and selection.
- **Reduce:** Aggregating data (e.g., computing a sum or product).

---

## 4. Magic Methods

### **What Are Magic Methods?**  
Magic methods (or dunder methods) are special methods that start and end with double underscores (e.g., `__init__`, `__str__`). They allow objects to implement or override built-in behavior (such as arithmetic operations, string representation, etc.).

### **Examples & Syntax:**

```python
class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    # Magic method for string representation
    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    # Magic method for adding two Vectors
    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    # Magic method for equality check
    def __eq__(self, other: 'Vector') -> bool:
        return self.x == other.x and self.y == other.y

v1 = Vector(2, 3)
v2 = Vector(5, 7)
print(v1)               # Output: Vector(2, 3)
print(v1 + v2)          # Output: Vector(7, 10)
print(v1 == Vector(2, 3))  # Output: True
```

### **Practical Use Cases:**  
- Customizing object behavior for mathematical operations.
- Enhancing debugging with meaningful string representations.
- Supporting comparisons and sorting of custom objects.

---

## 5. Asynchronous Programming

### **What Is Asynchronous Programming?**  
Asynchronous programming allows you to write code that runs concurrently without blocking, making it ideal for I/O-bound and high-level structured network code.

### **Key Concepts:**
- **async/await:** Keywords to define and manage asynchronous functions.
- **Event Loop:** Manages and schedules asynchronous tasks.

### **Syntax & Examples:**

```python
import asyncio

# An asynchronous function (coroutine)
async def say_hello(delay: int) -> None:
    await asyncio.sleep(delay)
    print("Hello after", delay, "seconds!")

# Running asynchronous functions
async def main():
    # Run tasks concurrently
    await asyncio.gather(say_hello(1), say_hello(2), say_hello(3))

# Python 3.7+ approach
asyncio.run(main())
```

### **Practical Use Cases:**  
- Non-blocking I/O (e.g., reading files, network requests).
- Web servers and network applications.
- Parallelizing independent tasks.

---

## 6. More itertools

### **What is itertools?**  
The `itertools` module provides fast, memory-efficient tools for creating iterators for looping. It is ideal for tasks that involve combinatorial constructs, infinite iterators, and advanced looping.

### **Examples & Syntax:**

```python
import itertools

# chain: Combine multiple iterables
combined = list(itertools.chain([1, 2], [3, 4]))
print("Chain:", combined)
# Output: Chain: [1, 2, 3, 4]

# permutations: All possible orderings of an iterable
perm = list(itertools.permutations([1, 2, 3], 2))
print("Permutations:", perm)
# Output: Permutations: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# cycle: Infinite iterator cycling through an iterable (example with break)
counter = 0
for item in itertools.cycle("AB"):
    print(item, end=" ")
    counter += 1
    if counter == 6:
        break
# Output: A B A B A B
```

### **Practical Use Cases:**  
- Generating combinations/permutations for puzzles or optimization problems.
- Merging multiple iterators.
- Creating infinite data streams with controlled termination.

---

## 7. Summary and Additional Topics

### **Other Advanced Tools:**
- **Context Managers:** Using the `with` statement for resource management (e.g., files, locks).
- **functools:** Provides higher-order functions like `lru_cache` for caching function results.

### **Overall Benefits of Advanced Topics:**  
- **Enhanced Code Efficiency:** Write shorter, more expressive code.
- **Better Abstraction:** Hide complexity behind simple interfaces.
- **Performance Improvements:** Optimize memory usage and responsiveness (especially with generators and async programming).

---

## 8. Practice Exercises

1. **List Comprehensions:**  
   Write a list comprehension that creates a list of even numbers between 1 and 50 and then use a generator expression to compute the sum of their squares.

2. **Decorator Challenge:**  
   Create a decorator that measures the execution time of any function it wraps. Test it on a function that sums numbers from 1 to n.

3. **Magic Methods:**  
   Implement a custom class `Fraction` that supports addition, subtraction, and equality using magic methods like `__add__`, `__sub__`, and `__eq__`.

4. **Async Function:**  
   Write an asynchronous function that fetches data from two URLs concurrently (simulate the fetch using `asyncio.sleep`) and prints their "content" once both are done.

5. **itertools Usage:**  
   Use `itertools.combinations` to list all unique pairs from a given list of numbers and then use `map` to compute the sum of each pair.

---

## 9. Conclusion

Advanced Python topics like comprehensions, decorators, generators, closures, higher-order functions, magic methods, asynchronous programming, and the itertools module empower you to write more elegant, efficient, and scalable code. They are key to tackling complex tasks and processing large data sets while keeping your code modular and maintainable. Happy coding, and keep exploring these powerful tools!

---

[![Prev Lecture](../../Previous.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%203%20-%20Advance%20Topics/017%20OOP%20Fundamentals)       [![Next Lecture](../../Next.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%203%20-%20Advance%20Topics/019%20Database%20and%20CRUD)