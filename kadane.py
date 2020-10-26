a=[-2,-3,4,-1,-2,1,5,-3]
msf=a[0]

for i in range(len(a)):
    maxend=0
    for j in range(i,len(a)):
        maxend=maxend+a[j]
        if(maxend>msf):
            msf=maxend
        
print(msf)        
