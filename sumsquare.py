l=int(input("Enter number of elements:"))
lst=[]
sum1=0
sum2=0
for i in range(0,l):
    ele=int(input("Enter the element:"))
    lst.append(ele)
if((l<=0)or(ele<=0)):
    print("invalid")
else:    
    for i in range(0,l):
        if(lst[i]%2==0):
            sum2=sum2+lst[i]**2
        else:
            sum1=sum1+lst[i]**2
l1=[sum1,sum2]
print(l1)
