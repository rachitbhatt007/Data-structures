n=int(input())
for i in range(2**n):
    f=format(i,'b')
    if(len(f)!=n and f[0]==0):
        for i in range(n-1):
            f.append('0')
            printf("first",f)
    if(len(f)!=n and f[0]==1):
        for i in range(n-1):
            f.insert(0,'0')
            printf("second",f)

         
            

    
            
            
    
    
