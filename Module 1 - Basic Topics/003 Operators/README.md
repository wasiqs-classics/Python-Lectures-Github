![Python Operators](https://technobrainz.in/wp-content/uploads/2022/11/python-operators-v2.jpg)

### 003: Operators and Expressions

#### Introduction
So far, we have learned how to create variables and check their data types. But what if you want to perform actions like adding numbers, comparing values, or combining text? That’s where **operators** come into play. Operators allow you to perform operations on variables and data types, creating **expressions** that produce new results. Understanding operators is crucial for writing effective and dynamic Python programs.

---

### What is an Operator?
An **operator** is a symbol that tells Python to perform a specific mathematical or logical operation. Operators act on **operands**, which are the values or variables involved in the operation.

**Example**:
   ```python
   # '+' is an operator, and '5' and '3' are operands
   result = 5 + 3
   print(result)  # Output: 8
   ```
In the above example, `+` is the operator that adds `5` and `3`.

---

### Python Operators

Here are some of the most commonly used operators in Python:

1. **Arithmetic Operators**
   - **Addition (`+`)**: Adds two values.
     ```python
     total_cost = 100 + 50  # Output: 150
     ```
     *Real-world example*: Calculating the total cost of items in a shopping cart.
   - **Subtraction (`-`)**: Subtracts the right operand from the left.
     ```python
     remaining_budget = 500 - 150  # Output: 350
     ```
     *Real-world example*: Calculating remaining budget after spending.
   - **Multiplication (`*`)**: Multiplies two values.
     ```python
     area = 10 * 5  # Output: 50
     ```
     *Real-world example*: Calculating the area of a rectangle.
   - **Division (`/`)**: Divides the left operand by the right, returns a float.
     ```python
     price_per_item = 100 / 4  # Output: 25.0
     ```
     *Real-world example*: Splitting a bill among friends.
   - **Floor Division (`//`)**: Divides and returns the integer part.
     ```python
     result = 10 // 3  # Output: 3
     ```
     *Real-world example*: Calculating the number of groups that can be made without leaving any leftovers.
   - **Modulus (`%`)**: Returns the remainder of division.
     ```python
     remainder = 10 % 3  # Output: 1
     ```
     *Real-world example*: Checking if a number is even or odd.
   - **Exponentiation (`**`)**: Raises the left operand to the power of the right.
     ```python
     squared = 4 ** 2  # Output: 16
     ```
     *Real-world example*: Calculating the square of a number.

2. **Comparison Operators**
   - **Equal (`==`)**: Checks if two values are equal.
     ```python
     is_equal = (5 == 5)  # Output: True
     ```
   - **Not Equal (`!=`)**: Checks if two values are not equal.
     ```python
     is_not_equal = (5 != 3)  # Output: True
     ```
   - **Greater Than (`>`)**: Checks if the left value is greater.
     ```python
     is_greater = (10 > 5)  # Output: True
     ```
   - **Less Than (`<`)**: Checks if the left value is smaller.
     ```python
     is_less = (5 < 10)  # Output: True
     ```
   - **Greater Than or Equal (`>=`)**: Checks if the left value is greater than or equal to the right.
     ```python
     is_eligible_for_scholarship = (gpa >= 3.5)  # Output: True if gpa is 3.5 or above
     ```
     *Real-world example*: Checking if a student qualifies for a scholarship.
   - **Less Than or Equal (`<=`)**: Checks if the left value is less than or equal to the right.
     ```python
     can_register = (age <= 18)  # Output: True for students 18 or younger
     ```
     *Real-world example*: Determining eligibility for a youth program.

3. **Logical Operators**
   - **AND (`and`)**: Returns `True` if both conditions are true.
     ```python
     is_eligible = (age >= 18 and has_license)  # Both conditions must be true
     ```
   - **OR (`or`)**: Returns `True` if at least one condition is true.
     ```python
     can_enter = (age >= 18 or has_permission)
     ```
   - **NOT (`not`)**: Reverses the logical state.
     ```python
     is_not_allowed = not is_allowed
     ```

4. **Assignment Operators**
   - **Assignment (`=`)**: Assigns a value to a variable.
     ```python
     x = 10
     ```
   - **Add and Assign (`+=`)**: Adds a value to the variable.
     ```python
     x += 5  # Equivalent to x = x + 5
     ```
   - **Subtract and Assign (`-=`)**: Subtracts a value from the variable.
     ```python
     x -= 2  # Equivalent to x = x - 2
     ```
   - Other assignment operators include `*=`, `/=`, `//=`, `%=` for multiplication, division, floor division, and modulus operations.

5. **Identity Operators**
   - **is**: Checks if two variables point to the same object.
     ```python
     x = [1, 2, 3]
     y = x
     print(x is y)  # Output: True
     ```
     *Real-world example*: Verifying if two references are pointing to the same data in memory.
   - **is not**: Checks if two variables point to different objects.
     ```python
     a = [1, 2, 3]
     b = [1, 2, 3]
     print(a is not b)  # Output: True (different objects)
     ```

6. **Membership Operators**
   - **in**: Checks if a value is present in a collection.
     ```python
     fruits = ["apple", "banana", "cherry"]
     is_present = "apple" in fruits  # Output: True
     ```
   - **not in**: Checks if a value is not present in a collection.
     ```python
     restricted_word = "error"
     print(restricted_word not in message)  # Output: True if "error" is not in message
     ```

7. **Operator Precedence**
   Operator precedence determines the order in which expressions are evaluated in Python. Operators with higher precedence are evaluated first.

   **Example**:
   ```python
   result = 10 + 5 * 2  # Output: 20 (Multiplication happens before addition)
   ```
   Here, `5 * 2` is evaluated first due to its higher precedence, resulting in `10 + 10`.

   To ensure specific order, use parentheses:
   ```python
   result = (10 + 5) * 2  # Output: 30 (Addition happens before multiplication)
   ```

   *Real-world example*: Calculating discounts or taxes in an e-commerce application where different operations are needed, like `final_price = base_price - (base_price * discount / 100) + shipping_fee`.

For more information on Python operators, you can read further on the [W3 Schools website](https://www.w3schools.com/python/python_operators.asp).

---

### Exercise: Practice What You’ve Learned
1. Write a Python expression to calculate the area of a circle given its radius.
2. Use a comparison operator to check if a number is even or odd.
3. Write a program that checks if a person is eligible for a senior citizen discount (age 60 or older).
4. Create a variable `x` and use assignment operators (`+=`, `-=`, `*=`) to change its value.
5. Use the `is` operator to check if two variables reference the same object.

---

### Conclusion
Operators are the building blocks that allow us to perform actions and make decisions with our variables. By mastering these, you’ll be able to create more complex expressions and control the flow of your programs. In the next lesson, we’ll dive deeper into **Conditional Statements**, which will help us build more dynamic programs that react to different inputs. Let's continue the journey!

---

[![Next Lecture](../../Previous.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%201%20-%20Basic%20Topics/002%20Variables%20and%20Data%20Types)       [![Next Lecture](../../Next.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%201%20-%20Basic%20Topics/004%20Conditional%20Statements)
