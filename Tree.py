class Tree:
    def __init__(self,data):
        self.data=data 
        self.left=None
        self.right=None 


    def insert(self,data):
        if data<self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left=Tree(data)    

        if data>self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right=Tree(data)


    def inorder(self):
        elements = []
        if self.left:
            elements += self.left.inorder()
        elements.append(self.data)

        if self.right:
            elements += self.right.inorder()
        return elements


def buildtree(arr):
    root=Tree(arr[0])
    for i in arr:
        root.insert(i)
    return root   


if __name__=="__main__":
    arr=[3,4,52,1,7,43,8]
    tree=buildtree(arr)
    print(tree.inorder())
      





