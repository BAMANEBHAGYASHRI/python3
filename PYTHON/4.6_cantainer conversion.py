#container conversoin

l=[12,23,45,67,98,"shruti"]
print(l)

a=tuple(l)   #list to tuple
print(a)

b=set(l)        #list to set
print(b)

t=("shruti",345,56,67)
print(t)

c=list(t)    #tuple to list
print(c)

d=set(t)    #tuple to set
print(d)

set={12,23,45,76,"amplifier"}
print(set)

e=list(set)  #set to list    
print(e)

f=tuple(set)  #set to tuple
print(f)
