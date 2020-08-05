class Node
{
    constructor(data)
    {
        this.data = data
        this.left = null;
        this.right = null;
    }
}

class bst
{
    constructor()
    {
        this.root = null;
    }

    insertnode(refrence_node,newnode)
    {
        if(refrence_node.data<newnode.data)
        {
            if(refrence_node.right === null)
            refrence_node.right = newnode
            else
            {
                this.insertnode(refrence_node.right,newnode)
            }
        }
        else{
            if(refrence_node.left === null)
            refrence_node.left = newnode
            else
            {
                this.insertnode(refrence_node.left,newnode)
            }
        }
    }

    insert(data){
        var newnode = new Node(data)
        if(this.root === null){
            this.root = newnode
        }
        else
            this.insertnode(this.root,newnode)
    }
    inorder(node){
        if(node !== null){
            this.inorder(node.left)
            console.log(node.data)
            this.inorder(node.right)
        }
    }
}

var binary_s_tree_obj = new bst()
binary_s_tree_obj.insert(89)
binary_s_tree_obj.insert(50)
binary_s_tree_obj.insert(19)
binary_s_tree_obj.insert(30)
binary_s_tree_obj.insert(39)
binary_s_tree_obj.insert(40)
binary_s_tree_obj.insert(69)
binary_s_tree_obj.insert(80)

binary_s_tree_obj.inorder(binary_s_tree_obj.root)
