![Python Collables](https://jeevangupta.com/wp-content/uploads/2024/04/Choosing-the-Right-Python-Data-Structure-1024x578.png)
### Lecture 007: Collectables in Python

---

#### Introduction to Collectables

In Python, **collectables** are data structures that store multiple items. Each collection type—**Lists**, **Dictionaries**, **Tuples**, and **Sets**—serves unique purposes and has its own properties, strengths, and limitations. By understanding these collectables, you’ll be able to choose the right one for your program’s needs and use each effectively.

#### Comparison of Python Collectables

| Feature                | List         | Dictionary      | Tuple         | Set            |
|------------------------|--------------|-----------------|---------------|----------------|
| **Mutability**         | Mutable      | Mutable         | Immutable     | Mutable        |
| **Ordering**           | Ordered      | Ordered (3.7+)  | Ordered       | Unordered      |
| **Duplicates Allowed** | Yes          | Keys: No, Values: Yes | Yes          | No             |
| **Indexed Access**     | Yes          | By Key          | Yes           | No             |
| **Use Case**           | Sequence of items | Key-value pairs | Fixed data | Unique items  |

---

### Lists

A **list** is an ordered, mutable collection. It’s ideal for storing a sequence of items that may change over time, such as a to-do list.

#### List Operations

1. **Creating a List**:
   ```python
   items = []  # Empty list
   groceries = ["milk", "bread", "eggs"]  # List with items
   ```

2. **Adding Items**:
   - `append()`: Adds an item at the end of the list.
   - `insert()`: Inserts an item at a specified position.
   
   ```python
   groceries.append("cheese")
   groceries.insert(1, "butter")  # Adds butter at index 1
   ```

3. **Accessing Items**:
   - By index or using slicing.
   
   ```python
   print(groceries[0])  # Output: milk
   print(groceries[1:3])  # Output: ['butter', 'bread']
   ```

4. **Removing Items**:
   - `remove()`: Removes the first occurrence of a specified item.
   - `pop()`: Removes and returns an item at a specified index (or the last item by default).
   
   ```python
   groceries.remove("bread")
   last_item = groceries.pop()  # Removes "cheese"
   ```

5. **Other Useful Methods**:
   - `sort()`: Sorts the list.
   - `reverse()`: Reverses the list.
   - `count()`: Counts occurrences of a specific value.

6. **Use Case Example**: Managing a shopping list where items can be added, removed, or sorted based on needs.

---

### Dictionaries

A **dictionary** is a mutable collection of key-value pairs, ideal for storing associated data, such as user profiles or configurations.

#### Dictionary Operations

1. **Creating a Dictionary**:
   ```python
   student_cv = {}  # Empty dictionary
   student_cv = {"name": "Alice", "age": 20}
   ```

2. **Adding and Modifying Items**:
   - `dictionary[key] = value` assigns a new or existing key with a value.

   ```python
   student_cv["skills"] = ["Python", "Data Analysis"]
   ```

3. **Nested Dictionaries**:
   - Useful for structuring complex data, like a CV with sections for skills, education, and work experience.

   ```python
   student_cv["education"] = {"college": "XYZ University", "degree": "BSc Computer Science"}
   ```

4. **Accessing Items**:
   - Using keys directly or `get()` to safely retrieve values.

   ```python
   print(student_cv["name"])  # Output: Alice
   print(student_cv.get("age", "N/A"))  # Output: 20
   ```

5. **Removing Items**:
   - `pop(key)`: Removes and returns a value associated with a key.
   - `del`: Deletes a key-value pair.
   
   ```python
   student_cv.pop("age")
   del student_cv["skills"]
   ```

6. **Other Useful Methods**:
   - `keys()`: Returns all keys.
   - `values()`: Returns all values.
   - `items()`: Returns all key-value pairs.

7. **Use Case Example**: Building a student CV with categories for education, work experience, and skills that can be updated over time.

---

### Tuples

A **tuple** is an ordered, immutable collection that’s ideal for fixed data sets where values don’t change, such as coordinates or configuration settings.

#### Tuple Operations

1. **Creating a Tuple**:
   ```python
   coordinates = (10.0, 20.5)
   ```

2. **Accessing Items**:
   - Similar to lists, tuples use indices.
   
   ```python
   x = coordinates[0]  # Output: 10.0
   ```

3. **Methods for Tuples**:
   - `count()`: Counts occurrences of a value.
   - `index()`: Returns the index of the first occurrence of a value.

4. **Use Case Example**: Storing fixed geographical coordinates or default system settings.

---

### Sets

A **set** is an unordered collection of unique items, making it perfect for cases where you want to eliminate duplicates or perform mathematical set operations.

#### Set Operations

1. **Creating a Set**:
   ```python
   unique_numbers = {1, 2, 3, 4}
   ```

2. **Adding and Removing Items**:
   - `add()`: Adds an item to the set.
   - `discard()`: Removes an item without error if the item doesn’t exist.
   
   ```python
   unique_numbers.add(5)
   unique_numbers.discard(2)
   ```

3. **Mathematical Set Operations**:
   - `union()`: Combines two sets.
   - `intersection()`: Returns items common to both sets.
   
   ```python
   set1 = {1, 2, 3}
   set2 = {2, 3, 4}
   print(set1.union(set2))  # Output: {1, 2, 3, 4}
   print(set1.intersection(set2))  # Output: {2, 3}
   ```

4. **Use Case Example**: Tracking unique items, such as IDs or unique tags in a system.

---

### Exercise

1. Create a list of tasks and add, modify, and remove tasks dynamically.
2. Build a nested dictionary to represent a student profile, with categories for name, age, courses, and skills. Add values to each section.
3. Write a program that uses a tuple to store default settings and print each setting.
4. Use sets to identify unique numbers in a list and then find the intersection with another set of numbers.

---

### Conclusion

Congratulations on completing the first module! You now have a solid understanding of Python's basics—variables, data types, operators, conditionals, loops, strings, numbers, and collectables. With these foundations, you can now try your hand at small projects. Here are a few suggestions:

1. **To-Do List**: Create a program that manages a to-do list with options to add, remove, and display tasks.
2. **Simple Student Management System**: Track and update student information using dictionaries.
3. **Basic Calculator**: Build a calculator that uses operators and loops to perform arithmetic calculations.
4. **Search Engine**: Create a basic search feature that looks for keywords within a list of text.

Good luck with your journey ahead! These skills will be the foundation for the more advanced modules to come.

[![Next Lecture](../../Previous.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%201%20-%20Basic%20Topics/006%20Strings%20and%20Numbers)       [![Next Lecture](../../Next.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%202%20-%20Intermediate%20Topics)
