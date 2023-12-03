#!/usr/bin/python3
# clear()
a = {1, 2, 3}
a.clear()
print(a)
#------------------------------
# union()
b = {"one", "two", "three"}
c = {"1", "2", "3"}
x = {"zero", "cool"}
print (b | c)
print(b.union(c, x))
#-------------------------------
# add()
d = {1, 2, 3, 4}
d.add(5)
d.add(6)
print(d)
#-------------------------------
# copy()
e = {1, 2, 3, 4}
f = e.copy()
e.add(6)
print (e)
print(f)
#-------------------------------
# remove()
g = {1, 2, 3 , 4}
g.remove(1)
# g.remove(7) that will print error
print(g)
#--------------------------------
# discard()
h = {1, 2, 3, 4}
h.remove(1)
h.discard(7)
print(h)
#-----------------------------------
# pop()
i = {"A", True, 1, 2, 3, 4, 5}
print(i.pop())
#-----------------------------------
# update()
j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(["HTML", "CSS"])
j.update(k)
print(j)
#-------------------------------------
