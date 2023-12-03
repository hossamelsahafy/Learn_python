#!/usr/bin/python3 
my_list = ["one", "two", "three", 1, 100, True]
print(my_list)
print(my_list[0])
print(my_list[-1])
print(my_list[1:4])
print(my_list[1:])
print(my_list[::2])
#-------------------------------------------------
# extend
a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["one", "two"]
a.extend(b)
a.extend(c)
print(a)
#-------------------------------------------------
# remove
x = [1, 2, 3, "Osama"]
x.remove("Osama") 
print(x)
#--------------------------------------------------
# sort()
y = [1, 2, 100, 120]
y.sort(reverse=True)
print(y)
#---------------------------------------------------
# reverse
z = [10, 1, 9, 89, 100, "osama", 100]
z.reverse()
print(z)
#---------------------------------------------------
