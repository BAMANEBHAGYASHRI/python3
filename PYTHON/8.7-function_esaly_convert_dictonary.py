n=[]
u=[]
for i in range(5):
    name=input("take ur name")
    UID=int(input("take UID"))
    n.append(name)
    u.append(UID)
d=dict(zip(n,u))
print(d)
for x in d.items():
    print(x)

#homework
n=[]
b=[]
for i in range(5):
    name=input("take ur name ")
    branch=input("take ur branch ")
    n.append(name)
    b.append(branch)
d=dict(zip(n,b))
print(d)
for a,b in d.items():
    print(a,b)

