# Lecture 008: Debugging and Error Handling in Python

**Introduction to Debugging**

> **An error is an issue in a program that prevents the program from completing its task. In comparison, an exception is a condition that interrupts the normal flow of the program. Both errors and exceptions are a type of runtime error, which means they occur during the execution of a program.** 

Programming inevitably involves errors, and debugging is the process of identifying and resolving them. Python provides a robust framework to handle errors gracefully, ensuring programs run smoothly even in unexpected situations. In this lecture, we’ll explore debugging techniques, error handling, and how to interpret error messages effectively.

![Courtesy: Data Camp.](https://images.datacamp.com/image/upload/v1677232088/Exception%20and%20error%20handling%20in%20Python.png)

---

### Types of Errors in Python

1. **Syntax Errors**: Occur when Python encounters invalid code syntax.
   ```python
   if True
       print("Missing colon!")  # SyntaxError: expected ':'
   ```

2. **Runtime Errors (Exceptions)**: Happen during program execution (e.g., dividing by zero, accessing a nonexistent list element).
   ```python
   x = 10 / 0  # ZeroDivisionError
   ```

3. **Logical Errors**: The code runs but produces incorrect results due to flawed logic. These don’t raise exceptions and require careful debugging to identify.

---

### Different types of exceptions in python:

In Python, there are several **built-in Python exceptions** that can be raised when an error occurs during the execution of a program. Here are some of the most common types of exceptions in Python:

* **SyntaxError:** This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
* TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
* **NameError:** This exception is raised when a variable or function name is not found in the current scope.
* **IndexError:** This exception is raised when an index is out of range for a list, tuple, or other sequence types.
* **KeyError:** This exception is raised when a key is not found in a dictionary.
* **ValueError:** This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.
* **AttributeError:** This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
* **IOError:** This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
* **ZeroDivisionError:** This exception is raised when an attempt is made to divide a number by zero.
* **ImportError:** This exception is raised when an import statement fails to find or load a module.

These are just a few examples of the many types of exceptions that can occur in Python. It’s important to handle exceptions properly in your code using try-except blocks or other error-handling techniques, in order to gracefully handle errors and prevent the program from crashing.

---


### Reading Tracebacks and Console Error Messages

When an error occurs, Python generates a **traceback** that shows the sequence of calls leading to the error. Understanding this output is crucial for debugging.

**Example Traceback**:
```plaintext
Traceback (most recent call last):
  File "example.py", line 4, in <module>
    print(10 / 0)
ZeroDivisionError: division by zero
```

**How to Interpret**:
- **File Name and Line Number**: Locate the error in the code.
- **Error Type**: Indicates the category of the error (e.g., `ZeroDivisionError`).
- **Error Message**: Provides additional details about what went wrong.

---

