class traversal:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    def __repr__(self):
        return f"{self.value}"

def insert(root,value):
    if root is None:
        return inorderBST(value)
    elif value<root.value:
        root.left=insert(root.left,value)
    else:
        root.right=insert(root.right,value)
    return root

def pre_order(n):
    if n is None:
        return []
    return [n.value]+pre_order(n.left)+pre_order(n.right)

def in_order(n):
    if n is None:
        return []
    return(in_order(n.left)+[n.value]+in_order(n.right))
def post_order(n):
    if n is None:
        return []
    return post_order(n.left)+post_order(n.right)+[n.value]


node=inorderBST(20)
insert(node,25)
insert(node,18)
insert(node,10)
insert(node,26)
insert(node,1)
print(node.__repr__())
print(in_order(node))
print(pre_order(node))
print(post_order(node))
