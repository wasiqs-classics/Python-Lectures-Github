![Modules](https://journaldev.nyc3.cdn.digitaloceanspaces.com/2017/07/Python-Modules.png)

### Lecture 10: Modules in Python

---

#### Introduction

In Python, a **module** is a file containing Python code—such as functions, classes, or variables—that can be imported and utilized in other Python programs. Modules promote code reusability, organization, and maintainability by encapsulating related functionalities into separate files. This modular approach allows developers to manage complex codebases more efficiently and share functionalities across multiple programs. There are two kinds of modules:
- **Built-in Modules**: Provided by Python (such as `math`, `os`, and `sys`).
- **Custom Modules**: Modules you create yourself to encapsulate your own functions and variables.

---

### Benefits of Using Modules

- **Reusability**: modules enable the reuse of code across different programs without redundancy.
- **Maintainability**: eparating code into modules makes it easier to manage, update, and debug.
- **Namespace Management**: odules help prevent naming conflicts by encapsulating functions and variables within their own namespaces.
---

### Importing Modules

Python provides several ways to import modules:

1. **Importing an Entire Module**:
   ```python
   import math
   print(math.sqrt(16))  # Output: 4.0
   ```
   This imports the entire `math` module, allowing access to its functions using the `math.` prefix.
2. **Importing Specific Attributes from a Module**:
   ```python
   from math import pi, sqrt
   print(pi)         # Output: 3.141592653589793
   print(sqrt(16))   # Output: 4.0
   ```
   This imports specific functions or variables directly, eliminating the need for the module prefix.
3. **Importing All Attributes from a Module**:
   ```python
   from math import *
   print(sin(pi / 2))  # Output: 1.0
   ```
   This imports all functions and variables from the module into the current namespace. However, it's generally discouraged due to potential naming conflicts.
4. **Importing a Module with an Alias**:
   ```python
   import numpy as np
   array = np.array([1, 2, 3])
   print(array)  # Output: [1 2 3]
   ```
   This imports a module and assigns it a shorter alias for convenience.
---

### Creating a Module

To create a module:

1. **Write Python Code**: Define functions, classes, or variables in a `.py` file.
   ```python

   # mymodule.py

   def greet(name):
       return f"Hello, {name}!"

   pi = 3.14159
   ```
3. **Save the File**: ave the file with a `.py` extension, e.g., `mymodule.py`.
4. **Import and Use the Module**:
   ```python
   # main.py
   import mymodule

   print(mymodule.greet("Alice"))  # Output: Hello, Alice!
   print(mymodule.pi)              # Output: 3.14159
   ```
---

Let's create a more detailed example:

1. **Write Your Python Code**  
   Create a file (e.g., `custom.py`) and include your functions, variables, and classes. For example:

   ```python
   # custom.py

   def custom_one():
       return "This is custom one."

   def custom_two():
       return "This is custom two."

   user = {
       "name": "Wasiq",
       "age": 36,
       "country": "Pakistan"
   }
   ```

2. **Save the File**  
   Since a module is just a Python file, ensure it ends with `.py`.

3. **Using the Module in Your Main Script**  
   To use the module, import it in your working Python file:

   ```python
   # main.py

   import custom

   # Calling functions from the custom module:
   print(custom.custom_one())  # Output: This is custom one.
   print(custom.custom_two())  # Output: This is custom two.

   # Accessing variables:
   user_age = custom.user["age"]
   print(user_age)  # Output: 36
   ```

---

### The `__name__` Variable and Module Execution

In Python, each module has a special built-in variable called `__name__`. When a module is run directly, `__name__` is set to `"__main__"`. This allows for code within the module to determine if it is being run as the main program or being imported elsewhere.
**Example**:
```python
# mymodule.py

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    # This block runs only if the module is executed directly
    print(greet("World"))  # Output: Hello, World!
```
      In this example, the `greet` function will only execute when `mymodule.py` is run directly, not when it's imported into another module.

      Check this video as well: [What does if __name__ == '__main__' do in Python?](https://www.youtube.com/watch?v=x5IbdKnvt6k)
---

### How Python Finds Modules

When you use an import statement like `import abc`, Python follows these steps:
- **Step 1**: Look up the name `abc` in the module cache (`sys.modules`).  
- **Step 2**: If not found in the cache, search through the list of built-in modules (the Python Standard Library).  
- **Step 3**: Next, search the directories listed in `sys.path` (which includes the current directory).  
- **Step 4**: Once found, bind the module to the specified name in your local namespace.  
- **Step 5**: If Python cannot locate the module, a `ModuleNotFoundError` is raised.

*Note*: PEP 8 recommends placing all import statements at the beginning of your file (after any module-level docstrings or comments).

---

### Absolute vs. Relative Imports

Python supports two types of imports—**absolute** and **relative**—which help you locate modules within your project.

#### Absolute Imports

- **Definition**: An absolute import specifies the full path from the project’s root folder.
- **Example Directory Structure**:
  ```
  project/
  ├── package1/
  │   ├── module1.py
  │   └── module2.py  # Contains a function `function1`
  └── package2/
      ├── __init__.py  # Contains a class `class1`
      ├── module3.py
      └── subpackage1/
          └── module5.py  # Contains a function `function2`
  ```
- **Examples**:
  ```python
  from package1 import module1
  from package1.module2 import function1
  from package2 import class1
  from package2.subpackage1.module5 import function2
  ```
  Absolute imports are preferred for their clarity and because they remain valid regardless of where the import statement is located.

#### Relative Imports

- **Definition**: A relative import specifies the module's location relative to the current file.
- **Syntax**: Uses dot notation, where:
  - A single dot (`.`) refers to the current directory.
  - Two dots (`..`) refer to the parent directory.
  - Three dots (`...`) refer to the grandparent directory, and so on.
- **Examples**:
  - In `package1/module1.py`, to import `function1` from `module2.py`:
    ```python
    from .module2 import function1
    ```
  - In `package2/module3.py`, to import `class1` and `function2`:
    ```python
    from . import class1
    from .subpackage1.module5 import function2
    ```
  Relative imports can make the code more concise but are sometimes less readable and can be problematic if the directory structure changes.

---

### Exploring Built-in Modules

Python comes with a rich standard library of built-in modules that provide various functionalities.

**Example**:
```python
import os

# Get the current working directory
cwd = os.getcwd()
print(f"Current Working Directory: {cwd}")
```
     This script uses the `os` module to retrieve and print the current working directory.
---

### Exercises

1. **Create a Custom Module**:
   - rite a module named `calculator.py` that includes functions for addition, subtraction, multiplication, and division. Then, write a separate script to import and use these functions.
2. **Utilize a Built-in Module**:
   - se the `datetime` module to display the current date and time in a formatted string.
3. **Explore the `random` Module**:
   - reate a script that uses the `random` module to generate a list of 10 random integers between 1 and 100, and then sorts the list in ascending order.
4. **Implement the `__name__ == "__main__"` Construct**:
   - odify the `calculator.py` module to include test cases that only run when the module is executed directly, not when imported.
5. **Alias and Variable Access**:  
   In a module named `data.py`, define a dictionary `user = {"name": "Wasiq", "age": 36, "country": "Pakistan"}`. Import this module with an alias and print the user's age.

6. **Absolute Import Example**:  
   Given a project with two packages (`package1` and `package2`), use absolute imports in a file inside `package2` to import a function from a module in `package1`.

7. **Relative Import Exercise**:  
   Using the same project structure, write a relative import in a module inside `package1` to import another function from the same package. Then, in `package2`, use relative imports to import classes or functions from its submodules.
---

By mastering modules, you enhance your ability to write organized, reusable, and maintainable Python code, paving the way for more efficient and scalable programming practices. Remember! Modules are the cornerstone of writing modular, maintainable, and reusable code in Python. By understanding how to create, import, and utilize both built-in and custom modules—as well as mastering absolute and relative import strategies—you lay the groundwork for building scalable projects. Practice these concepts through the exercises, and soon you’ll be well-prepared to manage larger codebases and packages. Happy coding!

[![Prev Lecture](../../Previous.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%202%20-%20Intermediate%20Topics/009%20Functions)       [![Next Lecture](../../Next.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%202%20-%20Intermediate%20Topics/011%20Pip%20-%20Package%20Manager)
