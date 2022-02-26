a=0
sum=0
per=0
for i in range(5):
    m=int(input("enter your value"))
    if(m<35):
        a=1
    sum=sum+m
per=sum/5

if(a==1):
    print("fail with ATKT")
elif(per>=75 and per<100):
    print("frist class with dist")
elif(per>=60 and per<75):
    print("frist class ")
elif(per>=50 and per<60):
    print("second class")
elif(per>=35 and per<50):
    print("pass")
elif(per>=0 and per<35):
    print("fail")
else:
    print("invalid marks")



