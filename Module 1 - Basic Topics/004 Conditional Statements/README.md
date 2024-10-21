![Python Conditioal Statements](https://www.gangboard.com/wp-content/uploads/2019/07/python-conditional-statements-1.jpg)
### 004: Conditional Statements

#### Introduction
In Python, **conditional statements** allow us to control the flow of our programs based on conditions. We use these statements to make decisions in our code, ensuring that certain actions are only performed if specific criteria are met. Conditional logic enables programs to become more dynamic and responsive, making it a crucial tool for any programmer.

In this lesson, we’ll explore how to use **if-else** statements, handle multiple conditions, employ logical operators, and even utilize ternary operators to write efficient, clean code.

---

### Types of Conditional Statements

1. **The `if` Statement**

   The `if` statement allows you to execute a block of code only if a specified condition is true.
   
   **Example**:
   ```python
   age = 18
   if age >= 18:
       print("You are an adult.")
   ```

   *Real-world example*: Checking if a user is old enough to vote.

2. **The `if-else` Statement**

   The `if-else` statement executes one block of code if the condition is true, and another block if it is false.
   
   **Example**:
   ```python
   age = 16
   if age >= 18:
       print("You are an adult.")
   else:
       print("You are a minor.")
   ```

   *Real-world example*: Deciding whether a user qualifies for adult or child pricing based on their age.

3. **The `if-elif-else` Statement**

   The `if-elif-else` structure is used to evaluate multiple conditions. If the first condition is false, the program moves on to the next one.
   
   **Example**:
   ```python
   marks = 75
   if marks >= 90:
       print("Grade: A")
   elif marks >= 75:
       print("Grade: B")
   else:
       print("Grade: C")
   ```

   *Real-world example*: Grading students based on their marks.

4. **Nested `if` Statements**

   Sometimes, we need to put an `if` statement inside another `if`. This is known as a **nested if**.
   
   **Example**:
   ```python
   age = 25
   has_license = True
   if age >= 18:
       if has_license:
           print("You can drive.")
       else:
           print("You need a license to drive.")
   ```

   *Real-world example*: Checking if a person is old enough and has the necessary qualifications to drive.

5. **Ternary Operators**

   A **ternary operator** is a shorthand for writing `if-else` in a single line. It's useful when you need a quick, simple conditional expression.
   
   **Syntax**:
   ```python
   result = "Adult" if age >= 18 else "Minor"
   print(result)
   ```
   *Real-world example*: Determining if someone is an adult or minor in one line of code.

---

### Real-World Example: Report Card Program

Let’s build a simple report card program that assigns a grade based on marks using a combination of conditional logic and operators.

```python
# Input marks
marks = 85

# Check conditions for grading
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

# Use ternary operator to print pass or fail message
pass_fail = "Pass" if marks >= 60 else "Fail"

# Print results
print(f"Marks: {marks}")
print(f"Grade: {grade}")
print(f"Result: {pass_fail}")
```

**Explanation**:
- The program takes the `marks` as input and assigns a grade based on different ranges using `if-elif-else`.
- A **ternary operator** is used to determine whether the student has passed or failed.

---

### Exercise

Try these tasks to test your understanding:

1. Write a Python program that checks if a number is positive, negative, or zero using conditional statements.
2. Create a program that determines if a person is eligible to vote based on age.
3. Using a nested `if`, write a program that checks if a user can log in based on their username and password.
4. Modify the report card program to also print a congratulatory message if the student receives an A grade.
5. Use a ternary operator to assign and print "Even" or "Odd" based on whether a number is even or odd.

---

### Conclusion

Conditional statements are the backbone of decision-making in programming. By mastering `if-else`, `elif`, and ternary operators, you can make your programs smarter and more dynamic. In the next lesson, we’ll explore **Loops**, which will allow you to repeat actions in your programs, automating tasks and making your code more efficient. Read more!

[![Next Lecture](../../Previous.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%201%20-%20Basic%20Topics/003%20Operators)       [![Next Lecture](../../Next.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%201%20-%20Basic%20Topics/003%20Operators)
