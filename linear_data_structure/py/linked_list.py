class node:
    def __init__(self,data,link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head == None:
            return True

    def append(self,value):
        new_node = node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            last_node = self.tail
            last_node.link = new_node
            self.tail = new_node
        print(value,"element inserted")

    def printlist(self):
        temp = self.head
        while temp!=None:
            print(temp.data)
            temp = temp.link

obj_linked_list = LinkedList()
obj_linked_list.append(50)
obj_linked_list.append(100)
obj_linked_list.append(150)

obj_linked_list.printlist()






