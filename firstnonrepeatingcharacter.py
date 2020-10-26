import collections
# n=input()
d=collections.defaultdict(int)
# c=0
# for i in n:
#     d[i]+=1

# print(d)
# for i in d:
#     if(d[i]==1 and c==0):
#         print("the first non repeating character is {}".format(i))
#         c=c+1
    


for i in range(1,27):
    d[chr(i+96)]=i

print(d)
print(d.keys())    