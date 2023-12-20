#!/usr/bin/python3
# --Practical-Email_Slice--
email0 = "Hossam@gmail.org"
email1 = "Hossam_Elsahafy@gmail.org"
print(email0[0:6])
print(email0.index("@"))
print(email0[0 : email0.index("@")])
print("=" * 50)
# -----------------------------------------------------------------------
print(email1[0:15])
print(email1.index("@"))
print(email1[0 : email1.index("@")])
print("=" * 50)
# -----------------------------------------------------------------------
the_name = input("what's your name ? ").strip().capitalize()
the_email = input("what's your email? ").strip()

User_Name = the_email[: the_email.index("@")]
Wep_site = the_email[the_email.index("@") + 1 :]


print("Hello {}, your email is {}".format(the_name, the_email))
print("\nYour Name is : {} \nyour Wep_Site is : {}".format(User_Name, Wep_site))
# ------------------------------------------------------------------------
