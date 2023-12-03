#!/usr/bin/python3
my_set = {"osama", "said", 100}
print(my_set)
#print(my_set[0]) that will print an error
my_set_two = {1, 2, 3, 4, 5}
print(my_set_two)
# print(my_set_two[0:]) that will print error
# my_set_three = {"osama", 100, 100.5, True, [1, 2, 3]} Unhashable type list
my_set_three = {"osama", 100, 100.5, True, (1, 2, 3)}
print(my_set_three)
my_set_four = {1, 2, "osama", "one", "osama", 1}
print(my_set_four)
#--------------------------------------------------------------------------------------
