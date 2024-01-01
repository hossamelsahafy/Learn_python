#!/usr/bin/python3
# Practical Membership Control
# List Of Admins
Admins_list = ["Reyad", "Fares", "Ramadan", "Ammar", "Amir"]
# login
name = input("Please Write Your Name ").strip().capitalize()
# If Name Is Admin
if name in Admins_list:
    print("Hello {}, Welcome Back!".format(name))
    option = input("Delete Or Update Your Name ").strip().capitalize()
    # update option
    if option == "Update" or option == "U":
        NewName = input("Write The New Name : ")
        Admins_list[Admins_list.index(name)] = NewName
        print(Admins_list)
    # delete option
    elif option == "Delete" or option == "D":
        Admins_list.remove(name)
        print(Admins_list)
    else:
        print("Wrong Option Try Again")
else:
    status = input("Not Admin, Do You Want To Become An Admin Y, N? ")
    if status == "Y":
        Admins_list.append(name)
        print("Congratulation {} Now You Are An Admin".format(name))
        print(Admins_list)
    else:
        print("Okay See You Next Time")
