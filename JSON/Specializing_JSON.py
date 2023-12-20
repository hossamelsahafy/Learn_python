#!/usr/bin/python3
import json


# Specializing JSON object decoding:
def as_person(dict):
    if "name" in dict and "age" in dict:
        return {"name": dict["name"], "Age": int(dict["age"])}
    return dict


json_string = '{"name": "John", "age": 30}'
data = json.loads(json_string, object_hook=as_person)
print(data)
print("=" * 50)
# -------------------------------------------------------------------------
