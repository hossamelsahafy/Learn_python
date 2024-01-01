#!/usr/bin/python3
# nested loop for
peoples = ["Reyad", "Fares", "Ammar", "Ramadan"]
skills = ["HTML", "Css", "JS"]
for name in peoples:
    print("{} skills is: ".format(name))
    for skill in skills:
        print(skill)
else:
    print("#" * 100)
# -----------------------------------------------------------
people = {
    "AMMAR": {"HTML": "50%", "CSS": "80%", "C": "90%"},
    "Reyad": {"Python": "70%", "Java": "60%", "C": "80%", "Embded": "100%"},
    "Saeed": {"HTML": "60%", "CSS": "70%", "C": "100%"},
}
# print(people["AMMAR"])
# print(people["AMMAR"]["HTML"])
for name in people:
    print("skills and progress for {} is: ".format(name))
    for skill in people[name]:
        print("{} => {}".format(skill.upper(), people[name][skill]))
# ---------------------------------------------------------------
