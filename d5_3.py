n=int(input("ENTER:"))
c=0
count=0
while(n>0):
    d=n%10
    c=c+d
    n=n//10
for i in range(1,c+1):
    if(i*i<=c):
        count=count+1
print("The perfect numbers:",count)
    
    
