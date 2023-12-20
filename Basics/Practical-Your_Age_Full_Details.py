#!/usr/bin/python3
# -- Practical - Your Age Full Details --
# input age
age = int(input("what 's your age? ").strip())
# print(type(age))
# get age in all time units
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print("you lived for")
print("Months that you lived :{} ".format(months))
print("weeks that you lived :{:,} ".format(weeks))
print("days that you lived :{:,} ".format(days))
print("hours that you lived :{:,} ".format(hours))
print("minutes that you lived :{:,} ".format(minutes))
print("seconds that you lived :{:,} ".format(seconds))
