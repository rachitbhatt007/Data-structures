import collections
n=input()
d = collections.defaultdict(int)
for i in n:
    if(i!=" "):
        d[i]=d[i]+1
for key in d:
    print(key,end="")
    print(d[key],end='')
