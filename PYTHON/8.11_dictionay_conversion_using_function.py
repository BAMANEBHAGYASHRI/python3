'''print("fuction useed to dictoniary convertion:")
def info(**a):
    print(a)
    for p,q in a.items():           #using the line by line display output
        print(p,q)
info(name="shruti", collage="grwpt",branch="cse",roll_nno=19103)'''

print("multiple students marks & precentage find using function & disctinary convertion:")
def students (**a):
    #print(a)
    lst=[]
    lst1=[]
    for i,j in a.items():
        print(i,j)
        sum=0
        lst1.append(i)
        for x in j:
            sum=sum+x
        #print(sum)
        p=sum/5
        print(sum,p)
        print(i,"precentage",p)
        lst.append(p)
    #print(lst,lst1)
    d=dict(zip(lst1,lst))
    #print(d)
    mvf=max_number(lst)
    print("max value form function", mvf)
    for p,q in d.items():
        if(q==mvf):
            print(p,q)
            print("congrutution",p)
            
def max_number(no):
    m_no=no[0]
    for i in range(1,len(no)):
        if(no[i]> m_no):
            m_no=no[i]
    print("max no is",m_no)
    return m_no
students(siddhi=[90,78,56,45,90],jyoti=[89,67,80,70,60],
         payal=[45,89,67,70,80],nikita=[90,78,98,79,69],
         pooja=[90,98,97,65,50])

