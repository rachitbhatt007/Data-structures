a=[2,4,5,8,9]
b=[9,5,2,4]
a.sort()
b.sort()
print(a)
print(b)
for i in range(len(a)-1):
    if a[i]!=b[i]:
        print("the missing number is {}".format(a[i]))
        c=1
if(c==0):
    print("the missing number is {}".format(a[len(a)-1]))
