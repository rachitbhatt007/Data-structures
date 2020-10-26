import itertools
n=input()
a=itertools.combinations(n,3)
y = [' '.join(i) for i in a] 
print(y)
