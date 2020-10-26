import collections
import operator #for sorting
d1=collections.defaultdict()
d2=collections.defaultdict()

for i in range(1,27):
    d1[chr(i+96)]=i
    d2[chr(i+64)]=i

# print(d1)
# print(d2)    

# d3={**d1,**d2}
# print(d3)

# d3=d1.copy()
# d3.update(d2)
# print(d3)


# d1.setdefault('aa', None)
# d=d1.setdefault('a')
# print(d)
# print(d1.items())

# print(sorted(d1,reverse=True))
# print(sorted(sorted(d1),key =operator.itemgetter(0)))


Countries={'india','Nepal','china'}
v=[1,2,3,4,5,6]
c_dict=dict.fromkeys(Countries)#provide null values with countires as key
del(c_dict['china'])
print(c_dict)
c_dict=dict.fromkeys(Countries,v)
print(c_dict)
v.append(8)
print(c_dict)
for k,v in c_dict.items():
    print(k,v)
l=[1,2,3]
l2=['a','b','c']
zip_list=zip(l,l2)
# print(list(zip_list))
(l1,l2)=zip(*zip_list)
print(l1)
print(l2)