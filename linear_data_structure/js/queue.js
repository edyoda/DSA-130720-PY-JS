class Queue
{
    constructor()
    {
        this.items = []
    }

    enqueue(element)
    {
        this.items.push(element)
    }

    dequeue()
    {
        return this.items.shift()
    }

    isempty()
    {
        if(this.items.length == 0)
        {
            return true
        }
        else{
            return false
        }
    }

    peek()
    {
        console.log(this.items[0])
    }

    printQueue()
    {   console.log("******************")
        for(var i=0;i<this.items.length;i++){
            console.log(this.items[i])
        }
        console.log("******************")
    }
}

obj_queue = new Queue()

obj_queue.enqueue(12)
obj_queue.enqueue(15)
obj_queue.enqueue(18)
obj_queue.enqueue(21)

obj_queue.printQueue()

obj_queue.peek()

obj_queue.printQueue()


