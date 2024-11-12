import json
data = {'name': 'Alice', 'age': 25}
json_data = json.dumps(data)
print(json_data)  # {"name": "Alice", "age": 25}
restored_data = json.loads(json_data)
