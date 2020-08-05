class Node:
    def __init__(self,data):
        self.data = data
        self.left  = None
        self.right = None

def insert(node,data):
    # empty tree
    if node is None:
        return Node(data)

    if data <= node.data:
        node.left = insert(node.left,data)
    else:
        node.right = insert(node.right,data)

    return node

def findmin(node):
    current = node

    while(current.left is not None):
        current = current.left

    return current
    
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def deletenode(root,data):
    if data < root.data:
        root.left = deletenode(root.left,data)
    elif data> root.data:
        root.right = deletenode(root.right,data)
    else:
        # case 1 and case 2
        if root.left is None:
            temp = root.right
            root = None
            return temp # why return temp?
        
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = findmin(root.right)
        root.data = temp.data
        root.right = deletenode(root.right,temp.data)
    
    return root

root = insert(None,50)
root = insert(root,40)
root = insert(root,30)
root = insert(root,80)
root = insert(root,70)
root = insert(root,90)
root = insert(root,45)
root = insert(root,85)

print("The whole bs tree")
inorder(root)

root = deletenode(root,80)
print("The tree without 80")
inorder(root)

root = deletenode(root,45)

print("The update tree after deleting 45")
inorder(root)




