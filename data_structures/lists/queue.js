class Node {
    constructor(value){
        this.value = value;
        this.nextNode = null;
    }
}

class Queue {
    constructor(){
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    push(value){
        const node = new Node(value);
        if(this.size == 0){
            this.head = node;
            this.tail = node;
            this.size += 1;
        }else{
            this.tail.nextNode = node;
            this.tail = node
            this.size += 1
        }  
    }

    shift(){
        if(this.size == 0){
            return;
        }
        const value = this.head.value;
        if(this.size == 1){
            this.tail = null
        }
        this.head = this.head.nextNode
        this.size -= 1
        return value;
    }

    recursivePrint(node){
        console.log(node.value);
        if(node.nextNode == null){
            return;
        }
        return this.recursivePrint(node.nextNode);
    }

    print(){
        if(this.size == 0){
            console.log(null);
            return null;
        }
        if(this.size == 1){
            console.log(this.head.value);
            return this.head.value;
        }
        return this.recursivePrint(this.head);
    }
}


const myQueue = new Queue();
myQueue.push(1)
myQueue.push(2)
myQueue.push(3)
myQueue.push(4)
myQueue.push(5)
myQueue.print()
myQueue.shift()
console.log("\n")
myQueue.print()
myQueue.shift()
console.log("\n")
myQueue.print()
myQueue.shift()
console.log("\n")
myQueue.print()
myQueue.shift()
console.log("\n")
myQueue.print()
myQueue.shift()
console.log("\n")
myQueue.print()


