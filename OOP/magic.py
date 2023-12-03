#!/usr/bin/python3
class skill:
    def __init__(self):
        self.skill = {"html", "css", "js"}

    def __str__(self):
        return f"this is my skills => {self.skill}"

    def __len__(self):
        return len(self.skill)

    def __append__(self):
        return 0

    def __add__(self):
        self.skill.add(skill)


profile = skill()
print(profile)
print(len(profile))

profile.skill.add("PHP")
profile.skill.add("MYSQL")

print(len(profile))
print(profile)
# print(profile.__class__)
# ---------------------------------------------------
# my_string = "osama"
# print(type(my_string))
# print(my_string.__class__)
# print(dir(str))
# print(str.upper(my_string))
