my_var = "Rayan"

print(type(my_var))

another_variable : str = "Wasiq"

age : int = 30

user : str = ""

def my_func(name : str) -> str:
    return f"Hello {name}"

# For working with collectables

from typing import List, Dict, Tuple, Set, Union,Optional

grocery_items : List[str] = ["Item1", "Item2", "Item3"]
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
coordinates: Tuple[float, float] = (35.6895, 139.6917)
unique_ids: Set[int] = {1, 2, 3}


def x_to_the_power_y (x : Union[int, float], y : Union[int, float]) -> Union[int, float]:
    return x**y 

print(x_to_the_power_y(10,4))
print(x_to_the_power_y(2.3,5.1))

def get_username(name: Optional[str] = None) -> str:
    return name if name is not None else "Anonymous"

print(get_username())
print(get_username("Wasiq"))

# print(my_func("Wasiq"))
