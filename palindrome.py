n = int(input())
l=[]
f=0
for i in range(10**(n-1),10**(n-1)+10):
    if(i%9==0):
        f=i
        break
for i in range(f,10**n,9):
    a=str(i)
    if(a==a[::-1] and '0' not in a) :
        l.append(int(a))
        
print(l)
b=sum(l)%17
print(b)        
