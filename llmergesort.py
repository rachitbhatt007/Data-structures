from LLQuestions import Node
from LLQuestions import Linklist
l=Linklist()
for i in range(5):
    l.insert(i)

def merge(f,s):
    a=f
    b=s
    if(a.next==None and b.next==None):
        if(a.data<b.data):
            a.next=b
        else:
            b.next=a 
    elif(a.next!==None and b.next==None):
        pass           


     

def mergesort(l.head):
    t=l.head
    if(l.head==None or t.next==None):
        return 
    
    mid=l.findmid()
    second=mid.next

    mid.next=None

    f=mergesort(l)
    s=mergesort(mid.next)

    sortedlist=merge(f,s)
    return sortedlist




def merge()