![cover](https://www.askpython.com/wp-content/uploads/2021/03/Duck-Typing-in-Python.png)

## Lecture 16: Python with Type Hints

### 1. Introduction to Type Hints

**Type hints** (or type annotations) were introduced to Python to make the code more readable and self-documenting. They allow you to explicitly declare the expected data types of variables, function parameters, return values, and even class attributes. Although Python remains a dynamically typed language (i.e., types are checked at runtime), type hints enable static analysis tools (like mypy) to catch potential errors before execution. They also improve code completion and navigation in modern IDEs.

**Benefits of Type Hints:**
- **Enhanced Readability:** Clear documentation of function signatures.
- **Early Error Detection:** Tools like mypy can catch mismatches between expected and actual types.
- **Better IDE Support:** Auto-completion and refactoring become more reliable.
- **Improved Collaboration:** Clear contracts help team members understand how functions and classes are meant to be used.

---

### 2. Using Type Hints with Variables, Functions, and Classes

#### **Variables**
Annotate variables by specifying their type after a colon.

```python
name: str = "Alice"
age: int = 25
height: float = 5.7
is_student: bool = True
```

#### **Functions**
You can annotate function parameters and return types using a colon for parameters and an arrow (`->`) for the return type.

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Example call:
print(greet("Alice"))  # Output: Hello, Alice!
```

#### **Classes**
Annotate class attributes and method signatures to clarify the expected types.

```python
class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def is_adult(self) -> bool:
        return self.age >= 18

# Example usage:
person = Person("Bob", 20)
print(person.is_adult())  # Output: True
```

---

### 3. Important Topics in Typing

- **Built-in Generic Types:**  
  You can use type hints with built-in collections such as `list`, `dict`, `tuple`, and `set`:
  ```python
  from typing import List, Dict, Tuple, Set

  names: List[str] = ["Alice", "Bob", "Charlie"]
  scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
  coordinates: Tuple[float, float] = (35.6895, 139.6917)
  unique_ids: Set[int] = {1, 2, 3}
  ```
- **Union and Optional:**  
  Use `Union` when a variable can be one of several types, and `Optional` when a value can be a specific type or `None`.
  ```python
  from typing import Union, Optional

  def square(num: Union[int, float]) -> Union[int, float]:
      return num * num

  def get_username(name: Optional[str] = None) -> str:
      return name if name is not None else "Anonymous"
  ```

- **Type Inference:**  
  While type hints add clarity, Python can infer types at runtime. Hints are optional but very useful for static analysis.

---

### 4. The `typing` Module and Additional Imports

The `typing` module provides many useful types for annotations. For example:

- **Union and Optional:** (as shown above)
- **List, Dict, Tuple, Set, etc.:** For specifying container types.

You might also encounter:
```python
from collections.abc import Iterator, Callable
from typing import Union, Optional
```

For a quick reference, check out the [MyPy Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) for more common patterns without diving into overly complex topics.

---

### 5. Duck Typing vs. Static Type Hints

**Duck Typing** is a core principle of Python where the type or class of an object is less important than the methods it defines or the behavior it exhibits. In other words, if it "quacks like a duck," it is treated as a duck, regardless of its actual type.

**Example of Duck Typing:**
```python
def process_items(items):
    for item in items:
        # We don't care what type item is, as long as it can be iterated over
        print(item)

# Works with any iterable (list, tuple, set, custom iterator)
process_items(["apple", "banana", "cherry"])
```

**Type hints**, on the other hand, provide a way to specify expected types. They do not change runtime behavior but help developers and static analyzers understand your code better. While Python continues to use duck typing at runtime, type hints add an extra layer of clarity.

---

### 6. Summary

- **Type Hints** are annotations that help document and verify expected data types.
- They improve code clarity, static analysis, and IDE support.
- You can annotate variables, function parameters, return types, and class attributes.
- The `typing` module and related imports (like `Iterator` and `Callable`) offer a range of tools to express complex types.
- Despite type hints, Python remains dynamically typed and follows duck typing principles.

---

### 7. Practice Exercises

1. **Function Annotation:**  
   Write a function `sum_list` that takes a list of integers and returns their sum. Annotate the parameters and return type.

2. **Optional Parameters:**  
   Create a function `greet_user` that accepts an optional string argument for a user’s name. If no name is provided, it should return `"Hello, Anonymous!"`.

3. **Class Annotations:**  
   Define a class `Car` with attributes `make` (string), `model` (string), and `year` (int). Include a method `age` that returns the age of the car (assuming the current year is 2024).

4. **Callable and Union:**  
   Write a function `apply_operation` that accepts a callable (a function) that takes an integer and returns an integer, and an argument that can be either an int or a float. Return the result of applying the callable to the argument. Use type hints to annotate this function.

---

## **Conclusion**

Type hints in Python bridge the gap between dynamic typing and the benefits of static type checking. They serve as powerful documentation tools and enable better error detection with tools like mypy, all while preserving the flexibility of duck typing. By incorporating type hints in your code, you make it easier to understand, maintain, and collaborate on complex projects. Happy coding!

[![Prev Lecture](../../Previous.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%202%20-%20Intermediate%20Topics/015%20File%20Handling)       [![Next Lecture](../../Next.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%203%20-%20Advance%20Topics)
