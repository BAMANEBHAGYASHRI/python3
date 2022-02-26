#range function

for  i in range(5):
    print(i)

for  x in range(10,20):
    print(x)

for  a in range(30,50,5):
    print(a)

#even & odd number uisng range function
for i in range(  20,30):
     if(i%2==0):
         print("even no ",i)
     else:
        print("odd no ",i)

#input  the 5 number and using append function
a=[]
for i in range(5):
    n=int(input("take a value "))
    a.append(n)
    print(a)
for  i in a:
    print(i)

#addition of appending value
a=[]
sum=0
for i in range(5):
    n=int(input("take a value "))
    sum=sum+n
    a.append(n)
print(a)
print(sum)
