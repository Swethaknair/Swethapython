yrs=float(input("enter a year:"))
yrs=int(yrs)
flag=0
if(yrs>1000):
    if(yrs%4==0):
        if(yrs%100==0):
            if(yrs%400==0):
                flag=1
            else:
                flag=0
        else:
            flag=1
    else:
        flag=0
    if(flag==1):
        print("It is a leap year")
        print("Next leap year:",yrs+4)
    else:
        print("It is not a leap year")
        if(yrs-1%4==0):
            print("Previous leap year:",yrs-1)
        elif(yrs-2%4==0):
            print("Previous leap year:",yrs-2)
        else:
            print("Previous leap year:",yrs-3)
else:
    print("Invalid")
