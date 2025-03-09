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