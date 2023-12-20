#!/usr/bin/python3
import json

# encoding python object to json:
data = {"name": "sa7med", "age": 30}
json_string = json.dumps(data)
print(json_string)
print("=" * 50)
# --------------------------------------
# DEcoding:
json_string = '{"name": "MEOW", "Age": 25}'
data = json.loads(json_string)
print(data)
print("=" * 50)
# -----------------------------------------
