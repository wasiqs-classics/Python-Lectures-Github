# OOP - Object Oriented Programming

# Classes and Objects

# Benefits
# Modularity - code in the form of modules that we can
# whenever we want. 
# Secure and memory efficient. 

# inheritance - we can use properties from other obj

# polymorphism - methods with same names but diff behaviors

# CLASSES - Blueprints to crete object
# Classes contains all the information about objects
# that will be created using the classes. 
# class contains names, attributes, methods & logics

# OBJECTS - objects are the actual things made using
# classes. 
# Example: The blueprint of a house is a class
# The actual house is the object

# Class defines attributes (data, variables) and methods (functions)

# class details -> can be public, protected, private. 

# Public -> Everything that can be accessed outside the 
# class code.
# 
# Private -> Can only be accessed within the class
# Protected -> Can be accessed within the class and in the
# derived classes as well. 
# 
# OOP CONTENTS:
# Basics (Creation of Classes and Objects)
# Encapsulation (private, public)
# Polymorphism
# Inheritance

# Class creation

# class SmartPhone:
#     def __init__(self, brand : str, model : str, price : float) -> None:
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def display_info(self) -> None:
#         print(f"Smartphone Specs: \nBrand: {self.brand}\nModel: {self.model}\nPrice: ${self.price}")

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def speak(self):
#         print("I am barking!")

# Creation of objects

# phone1 = SmartPhone("Apple", "iPhone 16", 1000)
# phone1.display_info()

# dog1 = Dog("Tommy", 5)
# print(dog1.name)
# print(dog1.age)

# dog1.speak()

# Encapsulation - building classes with data and methods but restricting access to certain data only. 

class SmartPhone:
    def __init__(self, brand : str, model : str, price : float) -> None:
        self.brand = brand
        self.model = model
        self.price = price
        self.__battery = 100 # private

    def display_info(self) -> None:
        print(f"Smartphone Specs: \nBrand: {self.brand}\nModel: {self.model}\nPrice: ${self.price}")

    # to access private data from the class, we have to create getter / setter methods. 

    def get_battery_health(self) -> int:
        return self.__battery
    
    def update_battery_health(self, health : int) -> None:
        if 0 <= health <= 100:
            self.__battery = health
        else:
            print("Error: Battery health has to be between 0 and 100")


cell_phone = SmartPhone("Samsung", "S25", 999)
cell_phone.display_info()
print(f"Original Battery Health: {cell_phone.get_battery_health()}")
cell_phone.update_battery_health(90)
print(f"Updated Battery Health: {cell_phone.get_battery_health()}")

print(type("Hello World"))

