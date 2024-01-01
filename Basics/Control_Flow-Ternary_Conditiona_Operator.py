#!/usr/bin/python3
# Ternary Conditional Operator
country = input("what 's is your country? ")
if country == "Egypt":
    print("the weather in {} is 15".format(country))
elif country == "KSA":
    print("the weather in {} is 20".format(country))
else:
    print("your country is not in the list")
# short if
Rate = 18
age = 18
# if age < 18:
#     print("movie is not good for you")
# else:
#     print("Movie is good for you happy watching")
print(
    "movie is not good for you"
    if age < Rate
    else "Movie is good for you, happy watching"
)
