![Python OOP](https://www.mtoag.com/wp-content/uploads/2023/12/opps.png)
## Python OOP: A Comprehensive Guide

### 1. Introduction to OOP

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes code into **classes** and **objects**.  
- **Classes** are blueprints that define attributes (data) and methods (functions) for objects.  
- **Objects** are instances of classes that represent real-world entities.

**Benefits of OOP:**  
- **Modularity:** Code is organized into reusable components.  
- **Encapsulation:** Data and methods are bundled together.  
- **Inheritance:** Classes can inherit attributes and methods from other classes.  
- **Polymorphism:** Objects of different classes can be treated as instances of the same class, especially when they share common behavior.

---

### 2. Classes and Objects

#### **Creating a Class and an Object**

A class in Python is defined using the `class` keyword. The special method `__init__` acts as a constructor to initialize new objects, and `self` represents the instance of the class.

```python
class Smartphone:
    def __init__(self, brand: str, model: str, price: float) -> None:
        self.brand = brand         # Public attribute
        self.model = model         # Public attribute
        self.price = price         # Public attribute

    def display_info(self) -> None:
        print(f"Smartphone: {self.brand} {self.model}, Price: ${self.price}")

# Creating an object (instance) of the Smartphone class
phone1 = Smartphone("TechBrand", "X100", 799.99)
phone1.display_info()  # Output: Smartphone: TechBrand X100, Price: $799.99
```

---

### 3. Encapsulation

**Encapsulation** means bundling data (attributes) and methods (functions) together, and restricting access to some of the object's components. In Python, we use underscores (`_` or `__`) to indicate private attributes.

```python
class Smartphone:
    def __init__(self, brand: str, model: str, price: float) -> None:
        self.brand = brand
        self.model = model
        self.price = price
        self.__battery_health = 100  # Private attribute

    def display_info(self) -> None:
        print(f"Smartphone: {self.brand} {self.model}, Price: ${self.price}")

    # Getter method for battery health
    def get_battery_health(self) -> int:
        return self.__battery_health

    # Setter method for battery health
    def update_battery_health(self, health: int) -> None:
        if 0 <= health <= 100:
            self.__battery_health = health
        else:
            print("Error: Battery health must be between 0 and 100.")

# Create an object and access private attribute via getter/setter
phone2 = Smartphone("GadgetPro", "Z200", 899.99)
phone2.display_info()
print("Battery Health:", phone2.get_battery_health())  # Output: Battery Health: 100
phone2.update_battery_health(85)
print("Updated Battery Health:", phone2.get_battery_health())
```

---

### 4. Inheritance

**Inheritance** allows one class (child) to inherit attributes and methods from another class (parent), promoting code reuse.

```python
class Smartphone:
    def __init__(self, brand: str, model: str, price: float) -> None:
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self) -> None:
        print(f"Smartphone: {self.brand} {self.model}, Price: ${self.price}")

# Derived class: AndroidPhone inherits from Smartphone
class AndroidPhone(Smartphone):
    def __init__(self, brand: str, model: str, price: float, android_version: str) -> None:
        super().__init__(brand, model, price)
        self.android_version = android_version

    # Overriding display_info to include android_version
    def display_info(self) -> None:
        super().display_info()
        print(f"Android Version: {self.android_version}")

# Create objects from base and derived classes
phone_base = Smartphone("TechBrand", "X100", 799.99)
phone_android = AndroidPhone("TechBrand", "X200", 899.99, "11.0")
phone_base.display_info()
print()
phone_android.display_info()
```

---

### 5. Polymorphism

**Polymorphism** allows different classes to use methods with the same name. This means you can call the same method on different objects, and each object can respond in its own way.

```python
# Continuing with our Smartphone example

class iPhone(Smartphone):
    def __init__(self, brand: str, model: str, price: float, ios_version: str) -> None:
        super().__init__(brand, model, price)
        self.ios_version = ios_version

    # Overriding display_info to include ios_version
    def display_info(self) -> None:
        super().display_info()
        print(f"iOS Version: {self.ios_version}")

# Function that takes any smartphone and displays its info
def show_phone_info(phone: Smartphone) -> None:
    phone.display_info()

# Create different smartphone objects
phone_android = AndroidPhone("TechBrand", "X200", 899.99, "11.0")
phone_iphone = iPhone("Apple", "iPhone 13", 999.99, "15.0")

# Demonstrating polymorphism
for phone in [phone_android, phone_iphone]:
    show_phone_info(phone)
    print("-----")
```

---

### 6. Data Abstraction

**Data Abstraction** focuses on exposing only essential features of an object while hiding the complex implementation details. Python uses abstract classes (from the `abc` module) to achieve this.

```python
from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass

class Smartphone(Device):
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model

    def turn_on(self) -> None:
        print(f"{self.brand} {self.model} is now ON.")

    def turn_off(self) -> None:
        print(f"{self.brand} {self.model} is now OFF.")

# Cannot instantiate Device directly
phone = Smartphone("GadgetPro", "Z200")
phone.turn_on()
phone.turn_off()
```

For more details on abstraction: I have added a [lecture here]() for further review. 

---

### 7. Summary

- **Classes & Objects:** Classes serve as blueprints and objects are instances of these classes.  
- **Encapsulation:** Combines data and methods, using private attributes to protect data.  
- **Inheritance:** Enables new classes to inherit properties from existing classes.  
- **Polymorphism:** Allows methods to be used interchangeably across different classes.  
- **Data Abstraction:** Hides complexity via abstract classes and methods.

---

### 8. Practice Exercises

1. **Create a Vehicle Class:**  
   - Define a `Vehicle` class with attributes like `make`, `model`, and `year`.  
   - Create a method `display_details` that prints these details.

2. **Subclass for Specific Vehicles:**  
   - Create a subclass `ElectricCar` that inherits from `Vehicle` and adds an attribute `battery_capacity`.  
   - Override the `display_details` method to include battery capacity.

3. **Polymorphic Behavior:**  
   - Create a function `show_details(vehicle: Vehicle)` that calls the `display_details` method.  
   - Instantiate different vehicles (e.g., `Vehicle`, `ElectricCar`) and demonstrate polymorphism.

4. **Abstract Class Implementation:**  
   - Create an abstract class `Appliance` with abstract methods `turn_on` and `turn_off`.  
   - Create subclasses such as `WashingMachine` and `Refrigerator` that implement these methods.

5. **Encapsulation Challenge:**  
   - Modify the `Vehicle` class to include a private attribute for `maintenance_cost` and add getter and setter methods.  
   - Demonstrate how to update and access the maintenance cost.

---

## **Conclusion**

Python’s OOP features empower you to write clean, modular, and reusable code. By mastering concepts like classes, objects, encapsulation, inheritance, polymorphism, and data abstraction, you build a strong foundation for creating complex applications. Practice with these exercises to deepen your understanding, and remember—OOP is all about modeling real-world entities in your code. Happy coding!

[![Prev Lecture](../../Previous.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%202%20-%20Intermediate%20Topics/016%20Python%20With%20Type%20Hints)       [![Next Lecture](../../Next.png)](https://github.com/wasiqs-classics/Python-Lectures-Github/tree/master/Module%203%20-%20Advance%20Topics/018%20More%20Advanced%20Topics)