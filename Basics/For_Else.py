#!/usr/bin/python3
# for_else
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in my_numbers:
    if number % 2 == 0:
        print("{} is even".format(number))
    elif number % 2 == 1:
        print("{} is odd".format(number))
else:  # the loop is finished
    print("That's all the numbers!")
print("#" * 50)
# --------------------------------------------------------
my_name = "Hossam"
for letter in my_name:
    print("[ {} ]".format(letter.upper()))
print("$" * 50)
# ---------------------------------------------------------
# loop for training
Range = range(1, 100)
for number in Range:
    print(number)
print("=" * 50)
# -----------------------------------------------------------
my_skills = {"HTML": "50%", "CSS": "20%", "PYTHON": "80%", "C": "60%", "Meow": "100%"}
# print(my_skills["C"])
# print(my_skills.get("PYTHON"))
for skill in my_skills:
    print("my progress in language {} is: {}".format(skill, my_skills[skill]))
