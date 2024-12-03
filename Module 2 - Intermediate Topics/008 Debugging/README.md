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

### Difference between Syntax Error and Exceptions

* **Syntax Errors:** As the name suggests this error is caused by the wrong syntax in the code. It leads to the termination of the program. 
    * **Example:** Like missing a colon in if statement.
* **Exceptions:** Exceptions are raised when the program is syntactically correct, but the code results in an error. This error does not stop the execution of the program, however, it changes the normal flow of the program.
    * **Example:** When we divide by zero. These types of errors catch exceptions. 

---

### Handling Exceptions Gracefully

Now that we have learned about errors and exceptions in Python. We will learn to handle them by using try, except, else, and finally blocks. 
But wait?
> **What do we mean by handling them?** In normal circumstances, these errors will stop the code execution and display the error message. To create stable systems, we need to anticipate these errors and come up with alternative solutions or warning messages. 

### try and except Statement
The most simple way of handling exceptions in Python is by using the `try` and `except` block. Python uses `try-except` blocks to catch and handle exceptions without crashing the program.

1. Run the code under the `try` statement.
2. When an exception is raised, execute the code under the `except` statement. 

![Courtesy: Data Camp.](https://images.datacamp.com/image/upload/v1677232827/try%20and%20except%20in%20Python.png)

This approach might look similar to if else, but its more generic and catches all possible exceptions. 

1. **Basic Example**:
   ```python
   try:
       result = 10 / 0
   except ZeroDivisionError:
       print("You can't divide by zero!")
   ```
    This example will throw `ZeroDivisionError` and except block will catch it.

   ```python
    try:
       print(x)
    except:
       print("An exception has occurred!")
    ```
    This example will simply throw an exception because we haven't defined `x` yet.

2. **Catching Multiple Exceptions**:

    Now we will be using multiple `except` statements for handling multiple types of exceptions.    

   ```python
   try:
       x = int("abc")
   except (ValueError, ZeroDivisionError) as e:
       print(f"An error occurred: {e}")
   ```
   This example will display the same message for both types of errors. 
   
   ```python
   try:
    print(1/0)
   except ZeroDivisionError:
    print("You cannot divide a value with zero")
   except:
    print("Something else went wrong")
   ```
    * If a `ZeroDivisionError` exception is raised, the program will print *"You cannot divide a value with zero."*
    * For the rest of the exceptions, it will print *“Something else went wrong.”*
    
    
**Loading the file example**

Now, let’s look at a more practical example. 

In the code below, we are reading the CSV file, and when it raises the FileNotFoundError exception, the code will print the error and an additional message about the `data.csv` file. 

Yes, we can print default error messages without breaking the execution. 

```python
try:
   with open('data.csv') as file:
       read_data = file.read()
except FileNotFoundError as fnf_error:
   print(fnf_error)
   print("Explanation: We cannot load the 'data.csv' file")
```

3. **Using `else` and `finally`**:

![Courtesy: Data Camp.](https://images.datacamp.com/image/upload/v1677233590/try%20except%20else%20in%20Python.png)

We have learned about `try` and `except`, and now we will be learning about the `else` statement.

When the `try` statement does not raise an exception, code enters into the `else` block. It is the remedy or a fallback option when you expect a part of your script will produce an exception. It is generally used in a brief setup or verification section where you don't want certain errors to hide. 

**Note:** In the try-except block, you can use the `else` after all the `except` statements. 

   - **`else`**: Executes if no exception occurs.
   - **`finally`**: Executes regardless of exceptions.


   ```python
   a = int(input("Enter a: "))
   b = int(input("Enter b: "))
   try:
    result = a/b
   except ZeroDivisionError as err:
    print(err)
   else:
    print(f"Your answer is {result}")
   ```

---


