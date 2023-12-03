#!/usr/bin/python3
# clear()
user = {
    "name" : "osama"
}
print(user)
user.clear()
print(user)
print("=" * 40)
#--------------------------------
# update()
member = {
    "namme" : "osama"
}
print(member)
member["age"] = 36
print(member)
member.update({"Country" : "Egypt"})
print(member)
print("=" * 40)
#-------------------------------------
# copy()
main = {
    "name" : "Eren"
}
b = main.copy()
print(b)
main.update({"skills" : "Fighting"})
print(main)
print(b)
print("=" * 40)
#------------------------------------------
print(main.keys())
print(main.values())
#-------------------------------------------
