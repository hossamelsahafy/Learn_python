#!/usr/bin/python3
# Email Pattern ==> ^[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
import re

# Search Method That Will Make You Find One Capital Letter:
my_string = re.search(r"[A-Z]", "HossamWaleed")
print(my_string)
print(my_string.span())
print(my_string.string)
print(my_string.group())
print(100 * "=")
# ====================================================================
# Regular Expression For Email
# That Script To know If The Use Input Right Email Or not:
Is_Email = re.search(r"^[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)", "HO@hossam.com")
if Is_Email:
    print("It's Valid Email")
    print(Is_Email.span())
    print(Is_Email.group())
    print(Is_Email.string)
else:
    print("Please Enter Valid Email!")
print("=" * 100)
# =======================================================================
# If You want To Find All Capital Letters Use Find All Method
# Findall Method:
my_string = re.findall(r"[A-Z]", "Hossam Waleed EL")
print(my_string)
print("=" * 100)
# ======================================================================
# Advanced Email_Checker:
Input_Email = input("Please Input Your Email ")
search = re.findall(r"^[A-z0-9\.]+@[A-z0-9]+\.com|net|org|info", Input_Email)
List = []
if search != []:
    List.append(search)
    print("Email Added")
else:
    print("Please Input Valid Email")
for i in List:
    print(i)
