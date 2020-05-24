ihex=input()
ihex2=input()
a=bin(int(ihex, 16))[2:]
b=bin(int(ihex2, 16))[2:]

atd=(int(a,2))
btd=(int(b,2))
c=atd+btd
print(c)
d=bin(c)
print(d)
e=d[2:]
print(e)
   
        
        



