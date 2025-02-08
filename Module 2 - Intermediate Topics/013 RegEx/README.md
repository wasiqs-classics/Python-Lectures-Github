![Background](https://coderpad.io/wp-content/uploads/2022/04/coderpad-regex-the-complete-guide.jpg)

Please refer to [this link](https://github.com/wasiqs-classics/Code-Camp-Python-for-Data-Science-and-Machine-Learning/blob/master/Python%20Lect%2011%20-%20RegEx.pdf) for more info. 

### **Lecture: Regular Expressions (RegEx) in Python**  

---

## **1. Introduction to Regular Expressions**  

Regular Expressions (**RegEx**) are sequences of characters that define a **search pattern**. These patterns are used for **string validation, extraction, manipulation, and formatting** in textual data. Python provides the `re` module to work with regular expressions efficiently.

### **Why Use Regular Expressions?**  
- **String Validation**: Validate user inputs such as emails, phone numbers, and passwords.  
- **Data Extraction**: Extract specific information such as dates, phone numbers, or URLs from a text.  
- **Text Search and Replace**: Search for patterns in text and replace them with desired values.  
- **Data Cleaning**: Remove unwanted characters or correct text formatting.  
- **Log Analysis**: Extract timestamps, error codes, and messages from log files.  
- **Web Scraping**: Extract useful data from web pages (HTML/XML).  

---

## **2. Importing and Using RegEx in Python**  

To work with RegEx in Python, import the `re` module:  

```python
import re
```

### **Basic Example: Checking for a Pattern**
```python
pattern = r"^p....n$"
test_string = "python"

result = re.match(pattern, test_string)

if result:
    print("Pattern found!")
else:
    print("Pattern not found.")
```
💡 **Explanation**:
- `^` → The string must start with 'p'.
- `.` → Matches any character.
- `$` → The string must end with 'n'.
- ✅ `"python"` matches, but `"pokemon"` does not.

---

## **3. RegEx Meta Characters & Their Usage**  

Meta characters are special symbols in RegEx that help define patterns.  

| **Meta Character** | **Description** | **Example** | **Matches** |
|--------------------|----------------|-------------|-------------|
| `[]` | Matches any character inside brackets | `[aeiou]` | 'a', 'e', 'i', 'o', 'u' |
| `.` | Matches any character except a newline | `c.t` | 'cat', 'cut', 'cot' |
| `^` | Matches the beginning of a string | `^Hello` | 'Hello world' |
| `$` | Matches the end of a string | `world$` | 'Hello world' |
| `*` | Matches **0 or more** occurrences | `ab*` | 'a', 'ab', 'abb', 'abbb' |
| `+` | Matches **1 or more** occurrences | `ab+` | 'ab', 'abb', 'abbb' |
| `?` | Matches **0 or 1** occurrences | `colou?r` | 'color', 'colour' |
| `{}` | Matches a **specific range** of occurrences | `\d{2,4}` | '23', '234', '2345' |
| `()` | Groups expressions together | `(abc)+` | 'abc', 'abcabc' |
| `\|` | OR operator | `cat\|dog` | 'cat' or 'dog' |

---

## **4. Special Sequences in RegEx**  

Special sequences simplify RegEx patterns by using `\` followed by a character.  

| **Special Sequence** | **Description** | **Example** | **Matches** |
|----------------------|----------------|-------------|-------------|
| `\A` | Start of a string | `\APython` | 'Python is easy' |
| `\b` | Word boundary | `\bword\b` | 'word' but not 'wordy' |
| `\B` | Not a word boundary | `\Bword` | 'sword' but not ' word' |
| `\d` | Matches any digit (0-9) | `\d+` | '123', '4567' |
| `\D` | Matches any non-digit | `\D+` | 'hello', 'abc' |
| `\s` | Matches whitespace (space, tab, newline) | `\s+` | '   ', '\t' |
| `\S` | Matches non-whitespace | `\S+` | 'Hello', 'World' |
| `\w` | Matches alphanumeric characters | `\w+` | 'Python3' |
| `\W` | Matches non-alphanumeric characters | `\W+` | '!@#$', ' ' |
| `\Z` | End of a string | `Python\Z` | 'I love Python' |

---

## **5. Character Sets in RegEx**  

Character sets allow for flexible matching by specifying multiple characters inside square brackets.

| **Character Set** | **Description** | **Example** | **Matches** |
|------------------|----------------|-------------|-------------|
| `[abc]` | Matches 'a', 'b', or 'c' | `[aeiou]` | 'a', 'e', 'i', 'o', 'u' |
| `[a-z]` | Matches any lowercase letter | `[a-z]` | 'a', 'b', 'c', ..., 'z' |
| `[A-Z]` | Matches any uppercase letter | `[A-Z]` | 'A', 'B', 'C', ..., 'Z' |
| `[0-9]` | Matches any digit | `[0-9]` | '0', '1', ..., '9' |
| `[^abc]` | Matches any character **except** 'a', 'b', or 'c' | `[^0-9]` | Any non-digit |

---

## **6. Functions in the `re` Module**  

### **`re.search()`** – Finds the first occurrence
```python
import re

text = "I love Python 3.10"
match = re.search(r"\d+\.\d+", text)

if match:
    print("Version found:", match.group())  # Output: Version found: 3.10
```

### **`re.match()`** – Matches from the beginning of the string
```python
import re

match = re.match(r"Hello", "Hello world")
print(match.group())  # Output: Hello
```

### **`re.findall()`** – Returns all matches as a list
```python
import re

text = "There are 123 apples and 456 bananas."
numbers = re.findall(r"\d+", text)
print(numbers)  # Output: ['123', '456']
```

### **`re.sub()`** – Replaces patterns
```python
import re

text = "Java is great. Java is popular."
updated_text = re.sub(r"Java", "Python", text)
print(updated_text)  # Output: Python is great. Python is popular.
```

---

## **7. Practical Examples**  

### **Example 1: Validating an Email Address**
```python
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

print(is_valid_email("wasiqonly@gmail.com"))  # Output: True
```

### **Example 2: Validating a Phone Number (Pakistan Format: 03xx-xxxxxxxx)**
```python
import re

phone_pattern = r"^03\d{2}-\d{7}$"
phone = "0312-1234567"

if re.fullmatch(phone_pattern, phone):
    print("Valid phone number")
else:
    print("Invalid phone number")
```

### **Example 3: Extracting Dates**
```python
import re

text = "Meeting scheduled on 2024-05-15."
date_match = re.search(r'\d{4}-\d{2}-\d{2}', text)

if date_match:
    print("Meeting date:", date_match.group())  # Output: 2024-05-15
```

---

## **8. Exercises**  

1. Write a RegEx pattern to **validate passwords** (at least 8 characters, 1 uppercase, 1 lowercase, 1 number, 1 special character).  
2. Extract all **email addresses** from a given text.  
3. Validate **CNIC numbers** in the format `XXXXX-XXXXXXX-X`.  
4. Extract all **URLs** from a paragraph of text.  

---

## **9. Conclusion**  

Regular Expressions are a powerful tool for working with textual data in Python. They allow for pattern-based searching, validation, and manipulation of strings. Mastering RegEx will greatly enhance your text-processing capabilities in Python. 🚀

[![Prev Lecture](../../Previous.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%202%20-%20Intermediate%20Topics/012%20Some%20Important%20Packages)       [![Next Lecture](../../Next.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%202%20-%20Intermediate%20Topics/014%20JSON)
