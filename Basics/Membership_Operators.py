#!/usr/bin/python3
# string
name = "Hossam"
print("H" in name)
print("o" in name)
print("M" in name)
print("#" * 80)
# -----------------------------------
# list
friends = {"Reyad", "Ammar", "Khalid"}
print("Reyad" in friends)
print("Hossam" in friends)
print("Ammar" not in friends)
print("#" * 80)
# ------------------------------------
# Using in and not in with condition
countries_one = ["Egypt", "KSA", "Kuwait", "Bahrain"]
countries_one_discount = 80

countries_two = ["Italy", "USA"]
countries_two_discount = 50

my_country = "MEOW"
if my_country in countries_one:
    print("Hello You Have Discount Of ${}".format(countries_one_discount))
elif my_country in countries_two:
    print("Hello You Have Discount Of ${}".format(countries_two_discount))
else:
    print("Sorry! There Is No Discount For Your Country")
