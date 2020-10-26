class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None


    def insert(self,data):
        nn=Node(data)
        if(self.root==None):
            self.root=nn

        else:
            t=self.root
            while(t!=None):
                p=t
                if(data<t.data):
                    t=t.left
                else:
                    t=t.right
            if(data<p.data):
                p.left=nn
            else:
                p.right=nn    

    
    def inorder(self,root):
        if root.left:
            self.inorder(root.left)

        print(root.data,end=" ")

        if root.right:
            self.inorder(root.right)    
      

    def findmin(self,root):
        while(root!=None):
            min=root.data
            root=root.left
        return(min)       

    def findmax(self,root):
        while(root!=None):
            max=root.data
            root=root.right
        return(max)      



          

    def delete(self,root,value):
        
        if(root.data==value):
            print(root.right,root.left)
            if(root.left==None and root.right==None):
                return None
            elif(root.left==None):
                 root.right
            elif(root.right==None):
                return root.left
            else:
                print("I am in else")
                m=self.findmin(root.right)
                root.data=m
                root.right = self.delete(root.right,min)
                print(self.inorder(root))   

        elif(value<root.data):
            self.delete(root.left,value)
        elif(value>root.data):
            self.delete(root.right,value)


        




if __name__=="__main__":
    arr=[8,3,1,4,9,54,7]
    t=BST()
    for i in arr:
        t.insert(i)
    t.inorder(t.root)
    print("")
    print(t.findmin(t.root))
    print(t.findmax(t.root))
    print(t.delete(t.root,1))
       









