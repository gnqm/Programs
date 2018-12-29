x=["","one","two","three","four","five","six","seven","eight","nine"]
y=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
z=["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def ones(num):
    return (x[num])

def tens(num):
    if(num<10):
        return ones(num)
    elif(num>=10 and num<=19):
        return y[num%10]
    elif(num>=20 and num<=99):
        return (z[(num//10)-2] +' '+ x[num%10])

def hundreds(num):
    if(num<100):
        return tens(num)
    else:
        return (ones(num//100) + " hundred "+ tens(num%100))

def thousands(num):
    if(num<1000):
        return hundreds(num)
    else:
        return (tens(num//1000)+" thousand "+hundreds(num%1000))
        
def lakhs(num):
    if(num<100000):
        return thousands(num)
    else:
        return (tens(num//100000)+" lakh "+thousands(num%100000))

def crores(num):
    if(num<10000000):
        return lakhs(num)
    else:
        return (lakhs(num//10000000)+" crore, "+lakhs(num%10000000))
        
n=input("Enter number: ")
try:
    l=len(n.lstrip('0'))
    if(n.lstrip('0')==""):
        num=0
    else:
        num=int(n.lstrip('0'))

    if(num==0):
        print("Zero")
    else:
        print(crores(num))

except:
    print("Invalid Input, type a number having maximum 14 digits")
