n=int(input("enter the number"))
for i in range(2,int(n/2)):
    if n%i==0:
        print("prime number")
        break
else:
     print("not prime")
        
