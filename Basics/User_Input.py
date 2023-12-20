#!/usr/bin/python3
# User_Input
fname = input("what is your first name? ")
mname = input("whats is your mid name? ")
lname = input("whats is your last name? ")

fname = fname.strip().capitalize()
mname = mname.strip().capitalize()
lname = lname.strip().capitalize()

print("Hello {} {} {} Happy to see ya bro".format(fname, mname[0], lname))
