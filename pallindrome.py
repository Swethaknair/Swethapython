try:
    n=int(input("enter a number:"))
    temp=n
    rev=0
    if(n<=0):
        print("false")
    else:    
        while(n>0):
            a=n%10
            rev=rev*10+a
            n=n//10
        if(temp==rev):
            print("true")
        else:
            print("false")
except ValueError:
    print("Invalid")
