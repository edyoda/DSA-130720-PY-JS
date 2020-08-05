class Stack():

    def __init__(self):
        self.item = []

    def size(self):
        return len(self.item)

    def top(self):
        if len(self.item) >= 1:
            print(self.item[len(self.item) -1])
        else :
            print("Empty list")

    def pop(self):
        if len(self.item) >= 1:
            self.item.pop()
        else:
            raise IndexError 

    def push(self,item):
        self.item.append(item)
        print(self.item)

stack_obj = Stack()
stack_obj.push(34)
stack_obj.push(56)
stack_obj.top()