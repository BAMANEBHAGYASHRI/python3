#argumenet passing fixed value
def demo(name,age=18):
    print(name,age)
demo("shruti",18)
demo("bhagyashri")


print("_____Refrence_oprtor_____")
def function(a,b,c,d,*e):
    print(a,b,c,d,e)
function(12,23,34,54,56,67,78,98,0,9)

print("______ASSIGNMENT NO 1:_________")
def marks(a,*e):
    sum=a
    n=0
    for i in e:
        if(i<35):
            n=1
        sum=sum+i
    p=sum/5
    if(n==1):
        print("ATKT")
    elif(p>75 and p<=100):
        print("frist class with dist")
        print(p)                                       
    elif(p>60 and p<=75):
        print("frist class")
        print(p)
    elif(p>50 and p<=60):
        print("secnd class")
        print(p)
    elif(p>35 and p<=50):
        print("pass")
        print(p)
    elif(p>0 and p<=35):
        print("fail")
        print(p)
marks(90,78,45,90,67)
print("______ASSIGNMENT NO 2:_________")
def billing(z):
    print(z)
    sum=0
    for i in z:
        sum=sum+i
    print(sum)
    Gst=sum*0.018
    if(sum>100 and sum<500):
        amount=Gst+sum
        discount=sum*0.05
        total_amount=discount-amount
      
    elif(sum>500 and sum<1000):
        amount=Gst+sum
        discount=sum*0.10
        total_amount=discount-amount
      
    elif(sum>1000 and sum<1500):
        amount=Gst+sum
        discount=sum*0.15
        total_amount=discount-amount
      
    elif(sum>1500 and sum<2000):
        amount=Gst+sum
        discount=sum*0.05
        total_amount=discount-amount
    elif(sum>2000 and sum<2500):
        amount=Gst+sum
        discount=sum*0.05
        total_amount=discount-amount
    elif(sum>2500 and sum<3000):
        amount=Gst+sum
        discount=sum*0.05
        total_amount=discount-amount
    else:
        ("invalid value")
    
lst=[]
for i in range(400):
    a=int(input("enter your product "))
    lst.append(a)
    s=raw_input("do you want to continue ")
    
    if(s=="no"):
        break
billing(lst)


        
        

   
        


