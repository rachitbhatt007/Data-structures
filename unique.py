import collections
n=input()
d=collections.defaultdict(int)
c=0
for i in n:
    if(i!=" "):
        d[i]=d[i]+1
for i in d:
    if(d[i]>1):
        c=c+1
if(c==0):
    print("unique")
else:
    print("not unique")
        
