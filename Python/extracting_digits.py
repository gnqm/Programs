def digits(x,l):
    s=[]
    while(l>1):
        y=x%10
        s.append(y)
        x=x//10
        l=len(str(x))
    s.append(x)
    s.reverse()
    return s

n=input("Enter number: ")
try:
    l=len(n)
    num=int(n)
    a=digits(num,l)
    print(a)
except: 
    print("Not a number")