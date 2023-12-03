#!/usr/bin/python3
# clear
a = [1, 2, 3, 4]
a.clear()
print(a)
#-----------------------
# copy
b = [1, 2, 3, 4]
c = b.copy()
b.append(5)
print (b)
print(c)
#-------------------------
# count()
d = [1, 2, 2, 3]
print(d.count(2))
#-------------------------
#index
e = ["cat", "cow", "dog"]
print(e.index("dog"))
#-------------------------
# insert()
f = [1, 22, 5, 8]
f.insert(0, "test")
f.insert(-1, "Test")
print(f)
#--------------------------
# pop
g = [1, 2, 3, 4]
print(g.pop(-2))
#---------------------------
