#!/usr/bin/python3
# str
a = 10
print(type(a))
print(type(str(a)))
print("=" * 50)
# -----------------------
# tuple()
c = "Osama"  # string
d = [1, 2, 3, 4, 5]  # list
e = {"A", "B", "C"}  # set
f = {"A": 1, "B": 2}  # dictionary

print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))
print("=" * 50)
# ----------------------------
# list()
c = "Osama"  # string
d = (1, 2, 3, 4, 5)  # tuple
e = {"A", "B", "C"}  # set
f = {"A": 1, "B": 2}  # dictionary

print(list(c))
print(list(d))
print(list(e))
print(list(f))
print("=" * 50)
# --------------------------------
# set
c = "Osama"  # string
d = (1, 2, 3, 4, 5)  # tuple
e = {"A", "B", "C"}  # set
f = {"A": 1, "B": 2}  # dictionary

print(list(c))
print(list(d))
print(list(e))
print(list(f))
print("=" * 50)
# ----------------------------------
# set()
c = "Osama"  # string
d = (1, 2, 3, 4, 5)  # tuple
e = ["A", "B", "C"]  # list
f = {"A": 1, "B": 2}  # dictionary

print(set(c))
print(set(d))
print(set(e))
print(set(f))
print("=" * 50)
# -----------------------------------
# dict()
d = (("A", 1), ("B", 2), ("C", 3), ("D", 4), ("E", 5))  # tuple
e = [["one", 1], ["two", 2], ["three", 3]]  # list
# f = {{"A", 1}, {"B", 2}}  # set: unhashable type set
# g = "Hossam"  # to convert to dict it must me a key and value
print(dict(d))
print(dict(e))
print("=" * 50)
