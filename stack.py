class Stack:
    def __init__(self):
        self.top=-1
        self.l=[]

    def push(s,n):
        for i in n:
            if(i=="(" or i=="{" or i=="["):
                s.top=s.top+1
            else:
                s.top=s.top

    def pop(s,n):
        for i in n:
            if(i==")" or i=="}" or i=="]"):
                s.top=s.top-1
            else:
                s.top=s.top
    def conclusion(s):
        if(s.top==-1):
            print("1")
        else:
            print("0")

n=input()
s=Stack()
s.push(n)
s.pop(n)
s.conclusion()
                
            
