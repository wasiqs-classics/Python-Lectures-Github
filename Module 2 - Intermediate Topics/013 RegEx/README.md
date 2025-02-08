

## Lecture: Regular Expressions (RegEx) in Python

### 1. Introduction to RegEx

Regular Expressions (RegEx) are a powerful tool for pattern matching and text manipulation. They allow you to search, match, extract, and replace text based on complex patterns. Common use cases include data validation (e.g., email or phone number validation), text extraction, log file analysis, and more. In Python, the built-in `re` module provides functions to work with RegEx efficiently.

Please refer to (this link)[https://github.com/wasiqs-classics/Code-Camp-Python-for-Data-Science-and-Machine-Learning/blob/master/Python%20Lect%2011%20-%20RegEx.pdf] for more info. 

---

### 2. Importing and Basic Usage

To work with RegEx in Python, import the `re` module:
  
```python
import re
```

You can use various functions from `re` such as `search()`, `match()`, and `findall()` to find patterns in text. For example, to check if a pattern exists in a string:

```python
pattern = r"hello"
text = "hello world"
result = re.search(pattern, text)
if result:
    print("Pattern found!")
else:
    print("Pattern not found.")
```

---

### 3. Meta Characters and Special Sequences

#### Meta Characters  
These characters have special meanings in regular expressions:

- **`[]`**: Matches any single character inside the brackets.  
  *Example*: `[abc]` matches either `a`, `b`, or `c`.

- **`.`**: Matches any character except a newline.  
  *Example*: `a.c` matches `abc`, `aXc`, etc.

- **`^`**: Matches the start of the string.  
  *Example*: `^Hello` matches strings that start with "Hello".

- **`$`**: Matches the end of the string.  
  *Example*: `world$` matches strings that end with "world".

- **`*`**: Matches 0 or more repetitions of the preceding element.  
  *Example*: `ab*` matches `a`, `ab`, `abb`, etc.

- **`+`**: Matches 1 or more repetitions.  
  *Example*: `ab+` matches `ab`, `abb`, etc.

- **`?`**: Matches 0 or 1 occurrence of the preceding element (or makes quantifiers non-greedy).  
  *Example*: `colou?r` matches both `color` and `colour`.

- **`{}`**: Specifies an exact number or a range of occurrences.  
  *Example*: `\d{3}` matches exactly three digits.

- **`()`**: Groups expressions and captures the matched sub-pattern.  
  *Example*: `(abc)+` matches one or more occurrences of "abc".

- **`\|`**: Acts as an OR operator between multiple patterns.  
  *Example*: `cat|dog` matches either "cat" or "dog".

#### Special Sequences  
Special sequences provide shortcuts for common character sets:

- **`\A`**: Matches only at the start of the string.
- **`\B`**: Matches where `\b` does not, i.e., not at the word boundary.
- **`\b`**: Matches a word boundary (start or end of a word).
- **`\d`**: Matches any digit; equivalent to `[0-9]`.
- **`\D`**: Matches any non-digit.
- **`\s`**: Matches any whitespace character (spaces, tabs, newlines).
- **`\S`**: Matches any non-whitespace character.
- **`\w`**: Matches any alphanumeric character and underscore; equivalent to `[a-zA-Z0-9_]`.
- **`\W`**: Matches any character that is not alphanumeric or underscore.
- **`\Z`**: Matches only at the end of the string.

---

### 4. Character Sets and Their Use in RegEx

Within RegEx, **character sets** (defined using square brackets `[]`) allow you to match any one character from a specific set of characters. For example:
  
```python
pattern = r"[aeiou]"  # Matches any one vowel.
```

You can also define ranges:
  
```python
pattern = r"[a-z]"    # Matches any lowercase letter.
```

---

### 5. Key Functions in the re Module

- **`re.search()`**: Scans through a string and returns the first match.
  
  ```python
  match = re.search(r"\d+", "There are 123 numbers")
  if match:
      print(match.group())  # Output: 123
  ```

- **`re.match()`**: Checks for a match only at the beginning of the string.
  
  ```python
  match = re.match(r"Hello", "Hello world")
  if match:
      print("Match found")
  ```

- **`re.fullmatch()`**: Checks if the entire string matches the pattern.
  
  ```python
  match = re.fullmatch(r"\d{3}-\d{2}-\d{4}", "123-45-6789")
  if match:
      print("Valid format")
  ```

- **`re.findall()`**: Returns all non-overlapping matches as a list.
  
  ```python
  numbers = re.findall(r"\d+", "There are 123 numbers 456 here")
  print(numbers)  # Output: ['123', '456']
  ```

- **`re.finditer()`**: Returns an iterator yielding match objects over all matches.
- **`re.sub()`**: Replaces occurrences of the pattern with a specified replacement string.

---

### 6. Practical Examples

#### Example 1: Email Address Extraction

```python
import re

text = "Please contact us at support@example.com or sales@company.org."
pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
emails = re.findall(pattern, text)
print("Extracted emails:", emails)
# Output: Extracted emails: ['support@example.com', 'sales@company.org']
```

#### Example 2: Phone Number Validation (Format: 03xx-xxxxxxxx)

```python
import re

phone_pattern = r"^03\d{2}-\d{8}$"
phone = "0300-12345678"
if re.fullmatch(phone_pattern, phone):
    print("Valid phone number")
else:
    print("Invalid phone number")
# Output: Valid phone number
```

#### Example 3: CNIC Number Validation (Format: xxxxx-xxxxxxx-x)

```python
import re

cnic_pattern = r"^\d{5}-\d{7}-\d{1}$"
cnic = "12345-1234567-1"
if re.fullmatch(cnic_pattern, cnic):
    print("Valid CNIC")
else:
    print("Invalid CNIC")
# Output: Valid CNIC
```

#### Additional Example: Extracting All Phone Numbers from a Text

```python
import re

text = "Call me at 0300-12345678 or at 0311-87654321."
pattern = r"03\d{2}-\d{8}"
phone_numbers = re.findall(pattern, text)
print("Phone numbers found:", phone_numbers)
# Output: Phone numbers found: ['0300-12345678', '0311-87654321']
```

---

### 7. Conclusion

Regular Expressions in Python provide a robust method for handling text data. From validating formats such as emails, phone numbers, and CNICs to extracting meaningful data from large text blocks, mastering RegEx can significantly enhance your data processing and validation capabilities. Practice using the re module functions and experimenting with meta characters and special sequences to gain fluency. Happy pattern matching!

---

[![Prev Lecture](../../Previous.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%202%20-%20Intermediate%20Topics/012%20Some%20Important%20Packages)       [![Next Lecture](../../Next.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%202%20-%20Intermediate%20Topics/014%20JSON)