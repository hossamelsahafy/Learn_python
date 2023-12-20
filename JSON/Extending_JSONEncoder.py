#!/usr/bin/python3
import json


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, person):
            return {"name": obj.name, "age": obj.age}


person1 = person("jana", 22)
person2 = person("Jane", 26)
data = [person1, person2]
json_string = json.dumps(data, cls=CustomEncoder)
print(json_string)
