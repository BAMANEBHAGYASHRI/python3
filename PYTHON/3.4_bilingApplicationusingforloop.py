sum=0
for i in range(400):
    p=int(input("product of amount"))
    s=raw_input("do you want to cantinue ? ")
    sum=sum+p
    print(sum)
    if(s=="no"):
        break

if(sum>=100 and sum<=250):
    print("total payable amonut")
    dicount=sum*0.05
    amount=sum-dicount
    print("amount",amount)
    
elif(sum>=250 and sum<=450):
    print("total payable amonut")
    dicount=sum*0.010
    amount=sum-dicount
    print("amount",amount)
    
elif (sum>=450 and  sum<=700):
    print("total payable amonut")
    dicount=sum*0.015
    amount=sum-dicount
    print("amount",amount)
    
elif (sum>=700 and  sum<=1000):
    print("total payable amonut")
    dicount=sum*0.020
    amount=sum-dicount
    print("amount",amount)
    
    
elif(sum>=1000 and sum<=1500):
    print("total payable amonut")
    dicount=sum*0.025
    amount=sum-dicount
    print("amount",amount)
    
elif(sum>=1500 and sum<=2000):
    print("total payable amonut")
    dicount=sum*0.030
    amount=sum-dicount
    print("amount",amount)
    
else:
    print("invalid value")
    
    
    
        
        
