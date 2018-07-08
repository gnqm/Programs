def test(n):
    d=[]
    while(n>0):
        r=n%10
        d.append(r)
        n=n//10
    d.sort()
    return d
        
for i in range(1,499999):
    a=i*2
    b=test(a)
    c=test(i)
    if(c==b):
        print('{}*2={}'.format(i,a))