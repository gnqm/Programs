x=input("Type String (Eg:aaabbbaaabbabddccc):")
y=list(x)
print(y)
    
def abc(s):
    c=1
    ns=''
    for i,k in enumerate(s):
        if((i>0 and s[i]==s[i-1])):
            c+=1
            if(i==len(s)-1 and c%2==0):
                
                ns=s[0:i+1-c]
                print(ns)
        else:
            nc=c
            c=1
            if(nc%2==0):
                ns=s[0:i-nc]+s[i:]
                print(ns)
                break
    if(i==len(s)-1 and nc%2!=0):
        pass
    else:
        abc(ns)
  
abc(y)