#!/usr/bin/python3
# my_list = [1, 2, 3]
# print(my_list)
# print("=" * 50)
# my_list0 = [3, 4, 5]
# print(*my_list0)
def my_sum(x, y, z):
    print(x + y + z)


my_list = [1, 2, 3]
my_sum(*my_list)


def sum(*args):
    result = 0
    for x in args:
        result += x
    return result


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
print(sum(*list1, *list2, *list3))
print("=" * 50)
# ---------------------------------------


def sum(*args):
    result = 0
    for x in args:
        result += x
    return result


print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9))
print("=" * 50)
# -------------------------------------------

list = [1, 2, 3, 4, 5, 6]
a, *b, c = list
print(a)
print(b)
print(c)
my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
merged_list = [*my_first_list, *my_second_list]
print("=" * 50)
# ------------------------------------------------
my_first_dict = {"A": 1, "b": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dictionary = {**my_first_dict, **my_second_dict}
print(my_merged_dictionary)
print("=" * 50)
# -----------------------------------------------------
list_of_char = [*"islam", "7amo"]
print(list_of_char)
