import itertools
n= int(input())
l=[]
l1=[]
l2=[]
x=[int(x) for x in input().split()]
for i in range(1,len(x)+1):
    a=itertools.combinations(x,i)
    l1.append(a)

for i in range(len(x)):
    for j in l1[i]:
        l2.append(j)

c=0
for i in range(len(l2)):
    c0=0
    c1=0
    for j in range(len(l2[i])):
        a=bin(l2[i][j])[2:]
        a=(a.zfill(len(bin(max(x))[2:])))
        for k in a:
            if(k=='0'):
                c0=c0+1
            if(k=='1'):
                c1=c1+1            
    if(c0==c1):
        c=c+1
if(c==0):
    for i in range(len(bin(max(x))[2:])):
                   print('0',end="")
else:
    a=bin(c)[2:]
    a=(a.zfill(len(bin(max(x))[2:])))
    print(a)
                
            

         
