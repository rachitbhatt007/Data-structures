class Node:
    def __init__(self,data):
        self.data=data
        self.nxt=None

    def __str__(s):
        return str(s.data)


class llist:
    def __init__(self):
        self.head=None
        self.c=0

    def append(s,data):
        nn=Node(data)
        if(s.head==None):
            s.head=nn
        else:
            t=s.head
            while(t.nxt!=None):
                t=t.nxt
            t.nxt=nn
            
    def count(s):
        t=s.head
        while(t!=None):
            s.c=s.c+1
            t=t.nxt
        print("The Count is",s.c)    

    def lastfirst(s):
        prev=0
        t=s.head
        while(t.nxt!=None):
            prev=t
            t=t.nxt    
        prev.nxt=None    
        t.nxt=s.head
        s.head=t

    def reverse(s):
        t=0
        prev=None
        cur=s.head
        while cur:
            t=cur.nxt
            cur.nxt=prev
            prev=cur
            cur=t
        s.head=t
        print("Reversed list\n")

            
            
               
    def display(s):
        
         t=s.head
         while(t!=None):
             print(t)
             t=t.nxt
         


l=llist()
i="y"
while(i=="y"):
    a=int(input())
    l.append(a)
    ch=(input("dO u want to add more elements y/n:\n"))
    i=ch
l.display()
l.reverse()
l.display()
            
            
        
        
