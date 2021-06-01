print(str(True and False))
print(str(False and False))
print(str(False and True))
print(str(True and True))

print("\nOR\n")
print(str(True or False))
print(str(False or False))
print(str(False or True))
print(str(True or True))

print("\n")

print("Start of program")

chevy = False
ford = False
dodge = True
if (chevy or dodge or ford):
    if (chevy):
        print("car is a chevy!")
    elif (ford): #shorthand for else if
        print("car is a ford!")
    elif (dodge):
        print("car is a dodge!")
    else:
        print("car is unknown")
else:
    print("not a car")
print("End of program")
