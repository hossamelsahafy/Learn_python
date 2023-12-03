#!/usr/bin/python3
#-----------------
#--String_Methods

#index()
#index(substring, start, end)

a = "I Love Python"
print(a.index("P"))        # Index num 7
print(a.index("P", 0, 10)) #index num 7
# print(a.index("P", 0, 5))  # that will print Error
#--------------------------------------------------
#find
b = "I Love Python"
print(b.find("P"))        # Index num 7
print(b.find("P", 0, 10)) # index num 7
print(b.find("P", 0, 5))  # that will print -1
#---------------------------------------------------
#rjust() ljust()
c = "Hossam"
print(c.rjust(10))
print(c.rjust(10, "#"))
#---------------------------------------------------
d = "Hossam"
print(d.ljust(10))
print(d.ljust(10, "#"))
#---------------------------------------------------
#splitlines()
e = """First Line
second Line
third Line """
print(e.splitlines())
print(type(e.splitlines())) # to make sure that will print list

print("--------------------------")
f = "First Line\nSecond Line\nThird Line"
print(f.splitlines())
print(type(f.splitlines()))
#-------------------------------------------------------
# expandtabs()
g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(2))
#-----------------------------------------------------
#istitle()
one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())
print(two.istitle())
#------------------------------------------------------
# isspace()
three = " "
four = ""
print ("------------------")
print(three.isspace())
print(four.isspace())
#-------------------------------------------------------
#islower()
five = "i love python"
six = "I LOVE PYTHON"
print ("------------------")
print(five.islower())
print(six.islower())
#--------------------------------------------------------
seven = "Hossam_waleed"
eight = "hossam555"
nine = "meow--meow"
print ("------------------")
print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())
#-------------------------------------------------------
#isalpha()
x = "AaaaaaaBBBBBbbbb"
y = "jdbldbcldj5 65 1645"
print("---------------------")
print(x.isalpha())
print(y.isalpha())
#------------------------------------------------------
#isalnum()
f = "AaaaaaaBBBBBbbbb"
g = "jdbldbcldj561645"
print("---------------------")
print(f.isalnum())
print(g.isalnum())
#-------------------------------------------------------
