#magical_opertor
#print(int.__and__(2,2))
#print(int.__sub__(9,4))
class student:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("addition is:- ",self.a+self.b)

    def __add__(self, other):
        a=self.a+other.a
        b=self.b+other.b
        c=student(a,b)
        return c

a=student(20,54)
b=student(65,34)
c=a+b
#print(c)
print(a.a+b.b)

