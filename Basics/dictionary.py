#!/usr/bin/python3
# Dictionary:
user = {"Name" : "Osama",
        "age" : 30,
        "country" : "Egypt",
        "skills" : ["HTML", "Css", "JS"],
        "rating" : 10.5,
}
print(user)
print(user['country'])
print(user.get("country"))
print(user.keys())
print(user.values())
print("=" * 70) # separator
#--------------------------------------------------
# Two-Dimensional_Dictionary
languages = {
    "one" : {
        "Name" : "HTML",
        "progress" : "80%"
        },
    "Two" : {
        "Name" : "c",
        "progress" : "90%"
    },
    "Three" : {
        "Name" : "JS",
        "progress" : "95%"
    }
}
print (languages)
print (languages['one'])
print(languages['Three']['progress'])
print("=" * 70) # separator
#-----------------------------------------------
# dictionary len
print(len(languages))
print(len(languages["Two"]))
print("=" * 70) # separator
#-----------------------------------------------
# create dictionary from variables
frameworkone = {
    "name" : "Someone",
    "progress" : "80%"
}
frameworktwo = {
    "name" : "MEOW",
    "progress" : "85%"
}
frameworkthree = {
    "name" : "hamada",
    "progress" : "100%"
}
allframework = {
    "one" : frameworkone,
    "Two" : frameworktwo,
    "Three" : frameworkthree
}
print (allframework)
#---------------------------------------------
