#!/usr/bin/python3
# that is python codes to learn things about python
#====================================================
#--string method--
# split() rsplit()
a = "i love python "
print(a.split())

b = "i-love-python"
print(b.split("-"))

c = "i-love-python-and-php"
print(c.split("-", 3))

d = "i-love-python-and-php"
print(d.rsplit("-", 3))
# ----------------------------
# center()
e = "Hossam"
print(e.center(10))        #spaces
print(e.center(16, "#"))   #hashes
print(e.center(16, "@"))   #@
# -----------------------------
#count()
f = "I Love Python and PHP Becouse PHP is Easy"
print(f.count("PHP"))         # 2 PHP words
print(f.count("PHP", 0, 25))  # only one PHP word
#-------------------------------------------------------
#swapcase()
g = "I Love Python"
h = "i lOVE pYTHON"
print(g.swapcase())
print(h.swapcase())
#----------------------------------------------------------
#startwith()
i = "I Love Python"
print(i.startswith("I"))
print(i.startswith("s"))
print(i.startswith("p", 7, 12))
#----------------------------------------------------------
#endwith()
j = "I Love Python"
print ("------------------")
print(j.endswith("n"))
print(j.endswith("S"))
print(j.endswith("e", 2, 6))
#-------------------------------------------------------------
#--------------------------THE_END----------------------------




