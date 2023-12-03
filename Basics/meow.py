tries = 4
mainpasss = "zero123"
inputpasswoed = input("write ur password ")
while inputpasswoed != mainpasss :
    tries = tries - 1
    print(f"wrong pass, {'last' if tries == 0 else tries} chances left")
    inputpasswoed = input("write ur password ")
    if tries == 0:
        print ("try again later")
        break
        print ("will not print")
else:
    print ("Tez reyad 7amra")
#----------------------------------------------------
print("     _____||____")
print("    / =========== \\")
print("  /  ___      ___  \\")
print(" /  |   |    |   |  \\")
print("/___|___|____|___|___\\")
