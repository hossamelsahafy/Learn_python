#!/usr/bin/python3
# Loop Advanced Dictionary
my_skills = {"HTML": "50%", "CSS": "60%", "PYTHON": "80%"}
# print(my_skills.items())
for skill in my_skills:
    print("{} => {}".format(skill, my_skills[skill]))
print("#" * 50)
for key, value in my_skills.items():
    print("{} => {}".format(key, value))
print("#" * 50)
# ---------------------------------------------------------------------
My_Ultimate_Skills = {
    "HTML": {"Main": "60%", "pugjs": "80%"},
    "CSS": {"Main": "80%", "SASS": "90%"},
}
for main_key, main_value in My_Ultimate_Skills.items():
    print("{} progress is: ".format(main_key))
    for child_key, child_value in main_value.items():
        print("- {} => {}".format(child_key, child_value))
