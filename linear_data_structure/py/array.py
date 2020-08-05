class array:
    def __init__(self):
        self.length = 0
        self.data = []

    def getElementAtIndex(self,index):
        return self.data[index]

    def append(self,element):
        self.data.append(element)
        self.length+=1
        return self.length
    
    def pop(self):
        item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length-=1
        return item

    def deleteAt(self,index):
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length-=1
        return self.data
    
    def insertAt(self,index,item):
        for i in range(self.length,index,-1):
            self.data[i] = self.data[i-1]
        self.data[index] = item
        self.length+=1
        return self.data

array_obj = array()

array_obj.append(23)
array_obj.append(230)
array_obj.append(2300)
array_obj.append(230000)

print(array_obj.data)


array_obj.deleteAt(3)

print("array_obj has deleted an element at index 3")

print(array_obj.data)

print("array_obj[1] = ",array_obj.getElementAtIndex(1))

array_obj.deleteAt(1)

print("After deleting it looks like this",array_obj.data)


