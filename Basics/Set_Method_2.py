#!/usr/bin/python3
# difference()
a = {1, 2, 3, 4}
b = {1, 2, "osama", "Ahmed"}
print(a.difference(b)) # a - b
print(a)
print("=" * 40) #separator
#-------------------------------
c = {1, 2, 3, 4}
d = {1, 2, "osama", "Ahmed"}
print(c)
c.difference_update(d) # c - d
print(c)
print("=" * 40) #separator
#--------------------------------
#intersection()
e = {1, 2, 3, 4, "x", "osama"}
f = {"osama", "x", 2}
print(e)
print(e.intersection(f)) # e & f
print(e)
print("=" * 40) #separator
#-----------------------------------
#intersection_update()
g = {1, 2, 3, 4, "x", "osama"}
h = {"osama", "x", 2}
print(g)
g.intersection_update(h) # g & h
print(g)
print("=" * 40) #separator
#------------------------------------
# symmetric_difference()
i = {1, 2, 3, 4, 5, "x"}
j = {"osama", "hossam", 1, 2, 4, "x"}
print(i)
print(i.symmetric_difference(j)) #i ^ j
print(i)
print("=" * 40) #separator
#--------------------------------------
# symmetric_difference_update()
k = {1, 2, 3, 4, 5, "x"}
l = {"osama", "hossam", 1, 2, 4, "x"}
print(k)
k.symmetric_difference_update(l) #k ^ l
print(k)
print("=" * 40) #separator
#----------------------------------------
