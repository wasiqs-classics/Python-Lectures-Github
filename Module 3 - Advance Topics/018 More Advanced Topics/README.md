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

## 2. Decorators, Generators, Closures, and Higher-Order Functions

These concepts enhance how you structure and reuse your code.

### **Decorators**

#### **What Are They?**  
Decorators are functions that modify the behavior of other functions without permanently modifying them. They are useful for logging, access control, caching, and more.

#### **Syntax & Examples:**

```python
# A simple decorator that logs function calls
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger  # Decorator syntax
def add(a: int, b: int) -> int:
    return a + b

print(add(3, 5))
```
*Comments:*  
- The `logger` function wraps the `add` function to print details before and after its execution.

### **Generators**

#### **What Are They?**  
Generators are functions that yield values one at a time using the `yield` keyword. They allow lazy evaluation and can handle large data sets efficiently.

#### **Syntax & Examples:**

```python
# A generator that yields Fibonacci numbers up to n
def fibonacci(n: int):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

# Example usage:
for num in fibonacci(50):
    print(num, end=" ")
```

### **Closures**

#### **What Are They?**  
A closure is a function object that remembers values in enclosing scopes even if they are not present in memory. This allows inner functions to access variables of their enclosing function.

#### **Syntax & Example:**

```python
def make_multiplier(factor: int):
    def multiplier(n: int) -> int:
        return n * factor
    return multiplier

times3 = make_multiplier(3)
print(times3(10))  # Output: 30
```

### **Higher-Order Functions**

#### **What Are They?**  
These are functions that can accept other functions as arguments or return them as results. They form the basis of functional programming in Python.

#### **Example:**

```python
def apply_func(func, value):
    return func(value)

result = apply_func(lambda x: x ** 2, 5)
print("Square:", result)  # Output: Square: 25
```

### **Practical Use Cases:**  
- **Decorators:** For logging, access control, performance measurement, and caching.
- **Generators:** Processing large datasets, streaming data, and implementing pipelines.
- **Closures:** Capturing state and creating function factories.
- **Higher-Order Functions:** Passing behavior as parameters (e.g., callbacks).

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