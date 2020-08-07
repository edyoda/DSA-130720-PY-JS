class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def bfs(root):
    queue = []

    # empty tree
    if root is None:
        return

    queue.append(root)

    while(len(queue)>0):
        print(queue[0].data)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def preorder(root):
    if root is not None:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

def insert(node,data):
    # empty tree
    if node is None:
        return Node(data)

    if data <= node.data:
        node.left = insert(node.left,data)
    else:
        node.right = insert(node.right,data)

    return node

root = insert(None,50)
root = insert(root,40)
root = insert(root,30)
root = insert(root,80)
root = insert(root,70)
root = insert(root,90)
root = insert(root,45)
root = insert(root,85)

print("The inorder bs tree")
inorder(root)


print("The bfs traversal is")
bfs(root)

print("The postorder traversal is")
postorder(root)

print("The preorder traversal is")
preorder(root)



