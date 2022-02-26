
def students(*s):
    print(s)
    for i in s:
        a=0
        for j in i:
            a=a+j
        print(a)
        p=a/5
        print("precentage",p)
            
siddhi=[90,78,56,45,90]
jyoti=[89,67,80,70,60]
payal=[45,89,67,70,80]
nikita=[90,78,98,79,69]
pooja=[90,98,97,65,50]
students(siddhi,jyoti,payal,nikita,pooja)
 

