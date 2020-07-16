class array{
    constructor(){
        this.length=0;
        this.data = {};
    }

    getElementAtIndex(index){
        return this.data[index];
    }

    append(element){
        this.data[this.length]= element
        this.length++;
        return this.length;
    }

    pop(){
        const item = this.data[this.length-1];
        delete this.data[this.length-1];
        this.length--;
        return item;
    }

    deleteAt(index){
        for(let i=index;i<this.length-1;i++){
            this.data[i] = this.data[i+1];
        }
        delete this.data[this.length-1];
        this.length--;
        return this.data
    }

    insertAt(index,item){
        for(let i=this.length;i>=index;i--){
            this.data[i] = this.data[i-1];
        }
        this.data[index] = item;
        this.length++;
        return this.data;
    }
}

array_obj = new array();
array_obj.append(67);
array_obj.append(450);
array_obj.append(560);
array_obj.append(750);
console.log("length of the array is ",array_obj.length)

for(var key in array_obj.data){
    console.log(array_obj.data[key])
}

array_obj.pop()
console.log("After pop")
for(var key in array_obj.data){
    console.log(array_obj.data[key])
}

array_obj.deleteAt(1)

console.log("We have dleted an element at index 1")

for(var key in array_obj.data){
    console.log(array_obj.data[key])
}

array_obj.insertAt(1,500)
console.log("The element 500 is inserted at index 1")

for(var key in array_obj.data){
    console.log(array_obj.data[key])
}