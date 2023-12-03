#!/usr/bin/python3
class Member:
    not_allowed_names = {"Hall", "shit", "baloot"}
    users_num = 0

    def __init__(self, first_name, middle_name, last_name, gender):
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender
        Member.users_num += 1

    @classmethod
    def show_user_count(cls):
        print(f"we Have {cls.users_num} in our system")

    def full_name(self):
        if self.fname in Member.not_allowed_names:
            raise ValueError("First name is not allowed")
        else:
            return f"{self.fname} {self.mname} {self.lname}"

    def name_with_title(self):
        if self.gender == "Male":
            return f"Hello Mr {self.fname}"
        elif self.gender == "Female":
            return f"Hello Mrs {self.fname}"
        else:
            return f"{self.fname}"

    def get_all_info(self):
        return f"{self.name_with_title()}, your full name is: {self.full_name()}"

    def delete_user(self):
        Member.users_num -= 1
        return f"User {self.fname} Deleted"


print(Member.users_num)
mem_one = Member("ADAM", "angsh", "mangsh", "Male")
mem_two = Member("3ashora", "LLLL", "bbbbb", "Female")
mem_three = Member("said", "hhhhh", "NNNNNN", "Male")
mem_four = Member("Hal", "sht", "DD", "REyad")
print(Member.users_num)
# print(mem_one.fname, mem_one.mname, mem_one.lname)
# print(mem_two.fname, mem_two.mname, mem_two.lname)
# print(mem_three.fname, mem_three.mname, mem_three.lname)
# print(mem_one.full_name())
# print(mem_one.name_with_title())
# print(mem_two.full_name())
# print(mem_two.name_with_title())
# print(mem_three.full_name())
# print(mem_three.name_with_title())
print(mem_one.get_all_info())
print(mem_four.get_all_info())
print(mem_four.delete_user())
print(Member.users_num)
