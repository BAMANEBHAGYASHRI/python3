marks=int(input("take a marks"))
if(marks>0 and marks<35):
    print("fail")
elif(marks>=35 and marks<60):
        print("pass")
elif(marks>=60 and marks<75):
            print("dist")
elif(marks>=75 and marks<100):
             print("1st class with dist")
else:
    print("invalid marks")
