
l=[]
def add(item):
    l.append(item)

def prefix(pre):
    for i in l:
        if pre in i:
            print(i)


add('samridhi')
add('rachit')
add('aladin')
prefix('rac')
    