def odd_even():
    i=int(input("enter the number: "))
    if(i%2==0):
        print("even no ")
    else:
        print("odd no ")

def  prime():
    x=int(input("eneter the number: "))
    y=x//2
    z=0
    for i in range(2,x):
        if(x%i==0):
            z=1
            break
    if(z==1):
        print("not prime ")
    else:
        print("prime no ")
prime()
odd_even()
