try:
    n=int(input("enter the number:"))
    if(n>=0 and n<=9):
        print("Mirror image:")
        print(int(n)[::-1])
    if(n<0):
        print("INVALID NUMBER!")
except:
    print("OTHA PODA")
