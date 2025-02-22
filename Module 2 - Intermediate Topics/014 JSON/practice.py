import json

json_data = '{"name": "Alice", "age": 25, "email": "alice@example.com"}'

print(type(json_data))

# Converting JSON string to Python dictionary
python_dict = json.loads(json_data)

print(python_dict["name"])  # Output: Alice
print(type(python_dict)) 

data = {
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com",
    "skills": ["Python", "Machine Learning"]
}

json_formatted = json.dumps(data, indent=4, sort_keys=True)
print(json_formatted)


invalid_json = '{"name": "Alice", "age": 25}'  # Invalid JSON (single quotes)

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print("Error:", e)


