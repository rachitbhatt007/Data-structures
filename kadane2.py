n=int(input())
l=[]
for i in range(n):
    a=int(input())
    l.append(a)

msf=l[0]
d={}
maxend=0
fi=0
li=0
s=0
for i in range(n):
    maxend=maxend+l[i]
    if(msf<maxend):
        msf=maxend
        fi=s
        li=i
    if(maxend<0):
        maxend=0

        s=i+1

print(msf,fi,li)            

