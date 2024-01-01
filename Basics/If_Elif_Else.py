#!/usr/bin/python3
#  Control Flow - If, Elif, Else
# make decision
User_name = "Hossam"
Course_name = "python3"
User_country = "Meow"
Course_price = 100
if User_country == "Egypt":
    print("Hello {}, Because you are from {}".format(User_name, User_country))
    print(f'the course is "{Course_name}", price will be  {Course_price - 80}$')
elif User_country == "KSA":
    print("Hello {}, Because you are from {}".format(User_name, User_country))
    print(f'the course is "{Course_name}", price will be  {Course_price - 60}$')
else:
    print("Hello {}, Because you are from {}".format(User_name, User_country))
    print(f'the course is "{Course_name}", price will be  {Course_price - 30}$')
