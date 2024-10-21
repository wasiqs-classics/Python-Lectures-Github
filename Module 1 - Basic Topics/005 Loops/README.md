![Python Loops](3720240703115149.png)

### 005: Loops in Python

#### Introduction

In programming, loops are essential for automating repetitive tasks. Rather than manually writing the same piece of code multiple times, loops allow us to execute a block of code repeatedly based on a condition. Python supports two primary types of loops: **`for`** and **`while`** loops. By mastering loops, you can reduce redundancy and create more efficient programs.

In this lesson, we’ll explore these loops, along with key concepts like `break`, `continue`, and the `else` clause in loops.

---

### Types of Loops

#### 1. **`for` Loop**

A `for` loop is used to iterate over a sequence (like a list, tuple, or string) and perform an action for each item.

**Syntax**:
```python
for item in sequence:
    # code to execute
```

**Example (Real-world)**:
```python
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(f"Hello, {name}!")
```
*Real-world example*: Sending a greeting to each person in a list.

**Example (Pattern Generation)**:
```python
for i in range(1, 6):
    print("*" * i)
```
*Pattern generation*: This code prints a triangle of stars.

#### 2. **`while` Loop**

The `while` loop keeps running as long as a condition is `True`. It’s useful when you don’t know beforehand how many iterations are needed.

**Syntax**:
```python
while condition:
    # code to execute
```

**Example (Real-world)**:
```python
attempts = 3
while attempts > 0:
    password = input("Enter password: ")
    if password == "secret":
        print("Access Granted")
        break
    else:
        attempts -= 1
        print(f"Incorrect password. {attempts} attempts left.")
```
*Real-world example*: Password attempt system with limited retries.


---

### Special Loop Control Statements

#### 1. **`break` Statement**
The `break` statement exits a loop prematurely when a specific condition is met.

**Example**:
```python
for i in range(1, 11):
    if i == 6:
        break
    print(i)
```
*Explanation*: The loop prints numbers from 1 to 5, then exits when `i` equals 6.

#### 2. **`continue` Statement**
The `continue` statement skips the rest of the code inside the loop for the current iteration and moves to the next iteration.

**Example**:
```python
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
```
*Explanation*: The loop skips even numbers and only prints odd numbers.

#### 3. **The `range()` Function**

The `range()` function generates a sequence of numbers, which is useful for looping a specific number of times.

**Example**:
```python
for i in range(1, 6):
    print(i)
```
*Explanation*: This loop prints numbers from 1 to 5.

#### 4. **`else` Clause in Loops**

The `else` clause in loops executes once the loop completes all iterations without hitting a `break` statement.

**Example**:
```python
for i in range(5):
    print(i)
else:
    print("Loop completed!")
```
*Explanation*: The `else` block runs after the loop has iterated through all values.

---

### Nested Loops

A **nested loop** occurs when one loop is inside another. This allows us to perform more complex iterations, such as generating patterns or processing multi-dimensional data.

**Example**:
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()
```
*Explanation*: This code generates a grid of `(i, j)` pairs.

---

### Real-World Example: Multiplication Table
Let’s write a program to print a multiplication table using nested loops.

```python
# Multiplication Table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:2}", end=" ")
    print()
```
*Explanation*: The nested loops print a 5x5 multiplication table.

### Real-World Example: Restaurent Order System

```python

menu = {
    'Burger': 5.0,
    'Pizza': 8.0,
    'Salad': 4.5,
    'Water': 1.0
}

current_order = None
total = 0

while True:
    print("\nWelcome to the Restaurant")
    print("1. View Menu")
    print("2. Place Order")
    print("3. View Order")
    print("4. Checkout")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        print("\nMenu:")
        for item, price in menu.items():
            print(f"{item}: ${price:.2f}")

    elif choice == '2':
        item = input("\nEnter the item you want to order: ")
        if item in menu:
            current_order = item
            total = menu[item]  # Update total for the current item
            print(f"{item} added to your order.")
        else:
            print("Item not available.")

    elif choice == '3':
        if current_order:
            print(f"\nYour Order: {current_order} - ${total:.2f}")
        else:
            print("\nYou haven't placed an order yet.")

    elif choice == '4':
        if current_order:
            print(f"\nCheckout: {current_order} - ${total:.2f}")
            print(f"Total: ${total:.2f}")
            break  # Exit after checkout
        else:
            print("\nYou haven't placed an order yet.")

    elif choice == '5':
        print("\nThank you for visiting!")
        break  # Exit the loop

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")


```

## Output
![Screen 1](restaurent-screen1.png)
![Screen 2](restaurent-screen1.png)


## Pattern Making with Loops
Making pattern with loops is a great practice and we can leverage nested loops and some logics to generate some cool patterns using python. 
Here is a good video on this topic:

[![Watch the video](https://img.youtube.com/vi/k8SXsT5TLxQ/0.jpg)](https://www.youtube.com/watch?v=k8SXsT5TLxQ)

---

### Exercise

1. Write a program that prints all numbers from 1 to 20 using a `for` loop.
2. Using a `while` loop, print the even numbers between 1 and 10.
3. Create a triangle pattern using `for` loops:
   ```
   *
   **
   ***
   ****
   ```
4. Write a Python program that stops printing numbers once it reaches a number divisible by 7 using `break`.
5. Write a nested loop that prints the following pattern:
   ```
   1 2 3
   1 2 3
   1 2 3
   ```

---

### Conclusion

Loops are incredibly powerful tools that allow you to automate repetitive tasks and handle sequences of data efficiently. By learning to use `for` and `while` loops, as well as control flow tools like `break`, `continue`, and `range`, you'll be well-prepared to tackle more complex problems in Python.

In the next lesson, we’ll explore **string and numbers** even more. Keep practicing!

[![Next Lecture](../../Previous.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%201%20-%20Basic%20Topics/004%20Conditional%20Statements)       [![Next Lecture](../../Next.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%201%20-%20Basic%20Topics/006%20Strings%20and%20Numbers)
