class student:
    def __init__(self,**marks):
        self.marks=marks
    def calculate(self):
        for i,j in (self.marks).items():
            sum=0
            for x in j:
                sum=sum+x
            print(i, "total is:",sum)
            pre=sum/5
            print(i,"precentage is ",pre)
            





s=student(leena=[90,87,98,76,89],shivani=[90,87,76,65,90],
          pooja=[90,99,98,97,95],bhoomika=[99,98,98,99,99])
