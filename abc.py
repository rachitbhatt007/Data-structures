import itertools
x,y=map(int,input().split(" "))
c=0
l = []
l2 =[]
for i in range(x):
    a=(i**i)
    l.append(a)
for i in range(2,x):
    subs=set(itertools.combinations(l,i)) 
    l2=l2+list(subs)
for i in range (len(l2)):
    a=sum(l2[i])
    if(a%y)==0:
        c=c+1
print(c)        
