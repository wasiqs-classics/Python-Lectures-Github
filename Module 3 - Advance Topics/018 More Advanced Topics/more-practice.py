
# def outer_scope():
#     name = 'Wasiq'
#     city = 'Karachi'

#     def inner_scope():
#         print(f"Hello {name}, Greetings from {city}")

#     return inner_scope

# new_function = outer_scope()
# new_function()

# def make_multiplier(factor: int):
#     def multiplier(n: int) -> int:
#         return n * factor
#     return multiplier

# times3 = make_multiplier(3)
# print(times3(10))  # Output: 30

# # Closure sequence 
# # Out function is defined and it returns the reference to the inner function
# # then outer function is assigned to a variable which then referes to the inner function
# # when the new function is called, it calls the inner function which has access to the outer function's scope

# Decorators

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()

# Big picture
# Decorators are used to modify the behavior of function or class method

# Inner details
# when we call a function with decorators then the decorator basically calls the wrapper function which then modifies the original function being called with the decorator. 

# A simple decorator that logs function calls
# def decorator_function(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} with {args}, {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__} returned {result}")
#         return result
#     return wrapper

# @decorator_function  # Decorator syntax
# def base_function() -> None:
#     print("Calling base function")

# base_function()


# example - decorator function to check how much time a function took to execute

# import time

# def decorator_timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Function took {end_time - start_time} seconds to execute")

#     return wrapper

# @decorator_timer
# def counting_till_n(n):
#     summ = 0
#     for i in range(n+1):
#         summ += i
#     print(summ)

# counting_till_n(10000000)


# Generators

# def countdown(n: int):
#     while n > 0:
#         yield n
#         n -= 1

# counter = countdown(5)
# print(next(counter))  # Output: 5
# print(next(counter))  # Output: 4
# print(next(counter))  # Output: 3


import asyncio

# An asynchronous function (coroutine)
async def say_hello(delay: int) -> None:
    await asyncio.sleep(delay)
    print("Hello after", delay, "seconds!")

# Running asynchronous functions
async def main():
    # Run tasks concurrently
    await asyncio.gather(say_hello(1), say_hello(2), say_hello(3))

# Python 3.7+ approach
asyncio.run(main())

