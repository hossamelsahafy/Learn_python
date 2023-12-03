#!/usr/bin/python3
#replace()
a = "Hello one two three one one"
print(a.replace("one", "1"))
print(a.replace("one", "1", 1))
print(a.replace("one", "1", 2))
#----------------------------------------------
#join(Iterable)
mylist = ["Hossam", "Waleed", "Elsahafy"]
print("-".join(mylist))
print(" ".join(mylist))
print(", ".join(mylist))
print(type(", ".join(mylist)))
