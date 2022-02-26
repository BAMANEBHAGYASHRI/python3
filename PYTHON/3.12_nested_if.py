#ASSIGNMENT NO_2

#nested_if

age=int(input("take a age of voter"))
if(age>18):
    print("voter is eligible")
    verifty=input("do u have voter ID ?")
    if(verifty=="yes"):
        print("finally voted")
        print("thanks for vote")
    else:
        print("bring your voter ID")
else:
    print("voter is under age")
