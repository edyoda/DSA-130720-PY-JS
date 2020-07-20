 class Node {  
    constructor(element) 
    { 
        this.element = element; 
        this.next = null
    } 
}
class LinkedList { 
    constructor() 
    { 
        this.head = null; 
        this.size = 0; 
    }
    add(element) 
{ 
    var node = new Node(element); 
  

    var current; 
  
    if (this.head == null) 
        this.head = node; 
    else { 
        current = this.head; 
   
        while (current.next) { 
            current = current.next; 
        }
        current.next = node; 
    } 
    this.size++;
} 

getLast() {
    let lastNode = this.head;
    if (lastNode) {
        while (lastNode.next) {
            lastNode = lastNode.next;
        }
    }
    return lastNode;
}
getFirst() {
    return this.head;
}

printList() 
{ 
    var curr = this.head; 
    var str = ""; 
    while (curr) { 
        str += curr.element + " "; 
        curr = curr.next; 
    } 
    console.log(str); 
} 
  
} 

my_linked_list = new LinkedList();
my_linked_list.add(12);
my_linked_list.add(34);
my_linked_list.add(23);
my_linked_list.add(400);
console.log(my_linked_list.getLast());
console.log(my_linked_list.getFirst())
my_linked_list.printList()