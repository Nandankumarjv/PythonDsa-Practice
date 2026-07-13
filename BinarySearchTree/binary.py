class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    def __repr__(self):
        return f"{self.value}"


def insert(root,value):
        
        if root is None:
            return Node(value)
        elif value<root.value:
            root.left=insert(root.left,value)
        else:
            root.right=insert(root.right,value)

        return root
    
def find(root,target):
        if root is None or root.value==target:
            return root
        elif target<root.value:
            return find(root.left,target) 
        else:
            return find(root.right,target)
    

root=Node(50)
insert(root,49)
insert(root,59)
insert(root,69)
insert(root,9)
insert(root,19)
print(root.right)
print(root.left.left.right)

