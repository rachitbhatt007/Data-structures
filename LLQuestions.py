class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

import collections
class Linklist:
    def __init__(self,head=None):
        self.head=None

    def insert(self,data):
        nn=Node(data)
        if(self.head==None):
            self.head=nn
        else:
            t=self.head
            while(t.next!=None):
                t=t.next

            t.next=nn

    def count(self):
        c=0
        t=self.head
        while(t!=None):
            c=c+1
            t=t.next
        return c    


    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end=" ")
            t=t.next

    def reverse(self):
        nextnode=None
        prev=None
        cur=self.head
        while(cur!=None):
            nextnode=cur.next
            cur.next=prev
            prev=cur
            cur=nextnode 
        self.head=prev 

        self.display() 
        print("") 

    def nthTolast(self,n):
        t=self.head
        c=self.count()
        for _ in range(c-n):
            t=t.next
        print("\n",t.data) 


    def recllrev(self,cur,nextnode=None,prev=None):
        if(cur!=None):
            nextnode=cur.next
            cur.next=prev
            prev=cur
            cur=nextnode
            self.recllrev(cur,nextnode,prev)
        else:
            self.head=prev
            self.display()
                     
    def mergesort(self):
        pass

    def findmid(self):
        slow=self.head
        fast=self.head
        while fast.next:
            fast=fast.next
            if(fast.next):
                fast=fast.next
                slow=slow.next
        mid=slow.data
        print("\n",mid) 


    def sortremduplicate(self):
        t=self.head
        while(t.next!=None):
            
            if(t.data==t.next.data):
                t.next=t.next.next
                t=t.next
            else:
                t=t.next           
        self.display()

    def unsortduplicate(self):
        t=self.head
        t2=t.next
        prev=None
        while(t!=None):
            while(t2!=None):
                if(t.data==t2.data and prev.next.next!=None):
                    prev.next=prev.next.next
                    t2=t2.next
                elif(t.data==t2.data and prev.next.next==None):
                    t2.next=None
                
                else:
                    prev=t2
                    t2=t2.next        
            t=t.next
            if(t!=None):
                t2=t.next
    
        self.display()                

    def remdupdict(self):
        t=self.head
        d=collections.defaultdict(int)
        prev=None
        while(t!=None):
    
            d[t.data]+=1
            if(d[t.data]>1 and prev.next.next!=None):
                prev.next=prev.next.next
                t=t.next 
                
            elif(d[t.data]>1 and prev.next.next==None):
                prev.next=None    
                
            
            prev=t   
            t=t.next   
        self.display()  


          
            

if __name__=="__main__":
    n1=int(input("Enter no of elements"))
    ll=Linklist()
    ll2=Linklist()
    for i in range(n1):
        a=int(input())
        ll.insert(a)

    ll.display()
    print("")
    ll.remdupdict()
    # ll.unsortduplicate()
    # (ll.findmid())
    # ll.nthTolast(2)
    # ll.recllrev(ll.head)
    # print("")
    # ll.reverse()
    # ll.sortremduplicate()
    



    #----------------------------------------------------merge two link list alternate--------------------------------------

    # n2=int(input("\n Enter no of elements in second list \n"))
    # for i in range(n2):
    #     a=int(input())
    #     ll2.insert(a)

    # ll3=Linklist()
    # t1=ll.head
    # t2=ll2.head
    # m=max(ll.count(),ll2.count())
    # for i in range(m):
    #     if(i<ll.count()):
    #         ll3.insert(t1.data)
    #         t1=t1.next
    #     if(i<ll2.count()):
    #         ll3.insert(t2.data)
    #         t2=t2.next
    

    # ll3.display()
