s=input()
s1=input()
l=[]
d = {}
d1={}
for i in range(len(s)):
    l.append(s[i])
   
for i in s: 
    if i in d: 
        d[i] += 1
    else: 
        d[i] = 1

for i in s1: 
    if i in d1: 
        d1[i] += 1
    else: 
        d1[i] = 1
if(d==d1):
    print("anagram")
else:
    print("not an anagram")
    
        
