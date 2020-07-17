class Stack{
    constructor(){
        this.data = []
        this.top = -1
    }

    push(element){
        this.top = this.top+1
        this.data[this.top] = element
        console.log(element,"pushed at position",this.top)
    }

    head(){
        return this.data[this.top]
    }

    size(){
        return this.top+1
    }

    isEmpty(){
        if(this.top == -1){
            return true
        }
        else{
            return false
        }
    }
    pop() {
        if(this.isEmpty()){
            return "Stack is Empty"
        }
        var temp = this.data[this.top]
        this.top = this.top - 1
        console.log(temp,"Just popped and the value of top is ",this.top)
        return temp
    }
}

stack_obj = new Stack()
stack_obj.push(3)
stack_obj.push(63)
console.log("size of the stack is",stack_obj.size())
stack_obj.pop()
stack_obj.push(36)
stack_obj.pop()
console.log(stack_obj.head())