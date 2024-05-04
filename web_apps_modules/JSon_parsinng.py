import json
# ------------------------------------------------------------- #

# Python dictionary
python_data1 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convert dictionary to JSON string
json_data1 = json.dumps(python_data1)
print(json_data1)

# ------------------------------------------------------------- #

# JSON string
json_data2 = '{"name": "John", "age": 30, "city": "New York"}'

# Convert JSON string to Python dictionary
python_data2 = json.loads(json_data2)
print(python_data2["name"])

# ------------------------------------------------------------- #

# Nested JSON
json_data3 = '{"name": {"first": "John", "last": "Doe"}, "age": 30, "city": "New York"}'

# Convert JSON string to Python dictionary
python_data3 = json.loads(json_data3)
print(python_data3["name"]["first"])

# ------------------------------------------------------------- #

# JSON array
json_data = '[{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]'

# Convert JSON string to Python list of dictionaries
data = json.loads(json_data)
for person in data:
    print(person["name"], person["age"])
