#!/usr/bin/python3
# Control Flow - Nested If
# make decision
User_name = "Hossam"
Is_Student = "Yes"
Course_name = "python3"
User_country = "Qatar"
Course_price = 100
if User_country == "Egypt" or User_country == "KSA" or User_country == "Sudan":
    if Is_Student == "Yes":
        print(
            "Hello {}, Because you are from {} and student".format(
                User_name, User_country
            )
        )
        print(f'the course is "{Course_name}", price will be {Course_price - 90}$')
    else:
        print("Hello {}, Because you are from {}".format(User_name, User_country))
        print(f'the course is "{Course_name}", price will be {Course_price - 80}$')

elif User_country == "Qatar" or User_country == "ElBahrain":
    if Is_Student == "Yes":
        print(
            "Hello {}, Because you are from {} and student".format(
                User_name, User_country
            )
        )
        print(f'the course is "{Course_name}", price will be {Course_price - 60}$')
    else:
        print("Hello {}, Because you are from {}".format(User_name, User_country))
        print(f'the course is "{Course_name}", price will be {Course_price - 50}$')

else:
    print("Hello {}, Because you are from {}".format(User_name, User_country))
    print(f'the course is "{Course_name}", price will be {Course_price - 30}$')
