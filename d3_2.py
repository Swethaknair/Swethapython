n=int(input("Enter a number:"))
if(n>0 and n<=999):
    a=int(n/100)
    b=int(n%100)
    c=int(b/10)
    d=int(n%10)
    print(a,c,d)
    print(d,c,a)
    print(c,d,a)
    print(c,a,d)
    print(d,a,c)
    print(a,d,c)
if(n<0):
    print("POSITIVE NUMBERS ARE REQUIRED")
else:
    print("invalid")
