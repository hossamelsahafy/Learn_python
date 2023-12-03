#!/usr/bin/python3
user = {
    "name": "Osama"
}
print(user)
print(user.setdefault("Name", "Ahmed"))
print(user.setdefault("age", 36))
print(user)
print("=" * 60)
#-----------------------------------------------
#popitem()
member = {
    "name" : "osama",
    "skill" : "ps5"
}
print(member)
member.update({"age" : 36})
print(member)
print(member.popitem())
print("=" * 60)
#-------------------------------------------------
# items()
view = {
    "name" : "Osama",
    "skill": "xbox"
}
all_items = view.items()
print (view)
view["age"] = 36
print(all_items)
print("=" * 60)
#------------------------------------------------
# fromkeys()
a = ('mykey1', 'mykey2', 'mykey3')
b = ("x")
print(dict.fromkeys(a, b))
print("=" * 60)
#-----------------------------------------------
