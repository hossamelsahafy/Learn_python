#!/usr/bin/python3
# number = int(input("Write your Age: "))
# print (number)
# print(type(number))
#------------------------------------------
# try, except:
try: #try the code and test Errors
    number = int(input("Write your Age: "))
except: #handel the error if it founds
    print("that is not integer")
else: #if there is no  errors
    print("Good,  that  is integer")
finally:
    print("what ever it happens")
#-------------------------------------------
try:
    # print(1110 / 0)
    # print (X)
    print(int("hello"))
except ZeroDivisionError:
    print ("you can't divide by zero")
except NameError:
    print("name error")
except ValueError:
    print("error value")
except:
    print("Error Happens")




