def factorial (no):
    if(no==1):
        return 1
    
    return no*factorial(no-1)
    
a=factorial(5)
print(a)
