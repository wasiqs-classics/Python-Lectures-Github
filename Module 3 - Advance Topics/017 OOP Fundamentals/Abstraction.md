## **Abstraction in Python (Object-Oriented Programming - OOP)**  

### **1. What is Abstraction in Python?**  
**Abstraction** is one of the four fundamental principles of **Object-Oriented Programming (OOP)** (along with **Encapsulation, Inheritance, and Polymorphism**). It is used to **hide implementation details** and only expose the essential features of an object.

In **Python, abstraction is implemented using abstract classes and abstract methods**. This is done with the help of the **`ABC` (Abstract Base Class) module**.

### **2. Why Use Abstraction?**  
- **Hides Implementation Details:** Users only interact with high-level interfaces, without worrying about how things work internally.
- **Improves Code Maintainability:** Helps in designing cleaner APIs.
- **Encourages Code Reusability:** Common structures are defined in abstract classes, reducing redundancy.
- **Enhances Security:** Restricts access to certain details, preventing unintended modifications.

---

## **3. Implementing Abstraction in Python**  

### **3.1 Abstract Classes and Methods**
An **abstract class** is a class that cannot be instantiated directly. Instead, it serves as a blueprint for other classes. An **abstract method** is a method that is declared but **does not have an implementation** in the abstract class.

To create an abstract class in Python, we use the **`ABC` module** from `abc`.

### **Example: Abstract Class in Python**
```python
from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start_engine(self):
        """Abstract method - must be implemented by subclasses"""
        pass

    @abstractmethod
    def stop_engine(self):
        """Abstract method - must be implemented by subclasses"""
        pass

# Concrete class (subclass) implementing abstract methods
class Car(Vehicle):
    def start_engine(self):
        print(f"{self.brand} {self.model}'s engine is starting...")

    def stop_engine(self):
        print(f"{self.brand} {self.model}'s engine is stopping...")

# Creating an object of the subclass
my_car = Car("Toyota", "Corolla")
my_car.start_engine()  # Output: Toyota Corolla's engine is starting...
my_car.stop_engine()   # Output: Toyota Corolla's engine is stopping...
```

### **Explanation:**
1. **`Vehicle`** is an **abstract class**.
2. It has **two abstract methods**: `start_engine()` and `stop_engine()`, which must be implemented by any subclass.
3. **`Car`** is a **concrete subclass** that implements these abstract methods.
4. We can now create a **`Car`** object, but we **cannot instantiate `Vehicle` directly**.

**Trying to instantiate `Vehicle` will result in an error:**
```python
v = Vehicle("Generic", "Model")  
# TypeError: Can't instantiate abstract class Vehicle with abstract methods start_engine, stop_engine
```

---

## **4. Real-World Example: Bank Transactions (Abstract Class Example)**  

In this example, we will define an abstract class `BankAccount` and implement different account types (`SavingsAccount` and `CurrentAccount`).

```python
from abc import ABC, abstractmethod

# Abstract class
class BankAccount(ABC):
    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.balance = balance

    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        pass

# Concrete subclass - Savings Account
class SavingsAccount(BankAccount):
    def deposit(self, amount: float):
        self.balance += amount
        print(f"Deposited ${amount} in Savings Account. New Balance: ${self.balance}")

    def withdraw(self, amount: float):
        if self.balance - amount >= 100:  # Minimum balance restriction
            self.balance -= amount
            print(f"Withdrew ${amount} from Savings Account. New Balance: ${self.balance}")
        else:
            print("Insufficient balance! Minimum balance of $100 required.")

# Concrete subclass - Current Account
class CurrentAccount(BankAccount):
    def deposit(self, amount: float):
        self.balance += amount
        print(f"Deposited ${amount} in Current Account. New Balance: ${self.balance}")

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount} from Current Account. New Balance: ${self.balance}")
        else:
            print("Insufficient balance!")

# Creating account objects
savings = SavingsAccount("Alice", 500)
savings.deposit(200)
savings.withdraw(550)  # Should fail due to minimum balance rule

current = CurrentAccount("Bob", 800)
current.withdraw(900)  # Should fail due to insufficient balance
```

### **Why Use Abstraction Here?**
- **`BankAccount`** ensures that every bank account **must have deposit and withdraw methods**.
- **Different rules** for savings and current accounts are enforced in subclasses.
- Clients interact with **a common interface** without knowing implementation details.

---

## **5. Abstract Properties and Getters/Setters**

You can also create **abstract properties** in an abstract class.

```python
from abc import ABC, abstractmethod

class Device(ABC):
    @property
    @abstractmethod
    def device_type(self):
        """Abstract property"""
        pass

class Laptop(Device):
    @property
    def device_type(self):
        return "Laptop"

class Mobile(Device):
    @property
    def device_type(self):
        return "Mobile"

# Creating instances
laptop = Laptop()
mobile = Mobile()
print(laptop.device_type)  # Output: Laptop
print(mobile.device_type)  # Output: Mobile
```

---

## **6. Summary: Key Takeaways on Abstraction**

| **Feature**          | **Explanation** |
|----------------------|----------------|
| **Abstract Class**   | A class that **cannot be instantiated**. Acts as a blueprint. |
| **Abstract Method**  | A method declared but **not implemented** in the abstract class. Must be implemented in subclasses. |
| **ABC Module**       | `abc.ABC` is used to create abstract classes. |
| **Implementation**   | Subclasses must implement **all** abstract methods from the parent abstract class. |
| **Use Cases**        | APIs, UI designs, banking systems, device drivers, etc. |

---

## **7. Practice Exercises**

1️⃣ **Create an abstract class `Animal`**  
   - Define an abstract method `make_sound()`.  
   - Implement concrete classes `Dog` and `Cat` that provide their own implementations of `make_sound()`.  

2️⃣ **Create an abstract class `Shape`**  
   - Implement `Circle` and `Rectangle` subclasses that override a `calculate_area()` method.  

3️⃣ **Extend the Bank Account Example**  
   - Add an abstract method `calculate_interest()` and implement it differently for `SavingsAccount` and `FixedDepositAccount`.  

---

## **8. Conclusion**

Abstraction in Python helps in designing **flexible and maintainable code** by enforcing structure and hiding implementation details. By using **abstract classes**, we can define **common interfaces** while allowing different implementations in subclasses. This makes our code **more reusable, modular, and scalable**.

🚀 **Next Steps:** Try implementing abstraction in real-world projects like **e-commerce systems, authentication services, or simulation models**!