class Node {
    constructor(value) {
        this.value = value;
        this.nextNode = null;
    }
}

class Stack {
    constructor(){
        this.head = null;
        this.size = 0;
    }

    isEmpty(){
        return (this.head == null)
    }

    length() {
        return this.size;
    }

    printNode(node, list){
        if(node == null){
            console.log(list);
            return list;
        }
        list.push(node.value);
        return this.printNode(node.nextNode, list)
    }

    print(){
        const list = [];
        this.printNode(this.head, list)
        return list;
    }

    insertValue(node, newNode){
        if(node.nextNode == null){
            this.size += 1;
            return node.nextNode = newNode
        }
        return this.insertValue(node.nextNode, newNode);
    }
    
    push(value){
        const newNode = new Node(value);
        if(this.isEmpty()){
            this.size += 1;
            return this.head = newNode;
        }
        return this.insertValue(this.head, newNode);
    }

    removeNode(node){
        if(node.nextNode.nextNode == null){
            const removedValue = node.nextNode.value;
            this.size -= 1;
            node.nextNode = null;
            return removedValue;
        }
        return this.removeNode(node.nextNode);
    }

    pop(){
        if(this.head == null){
            return null;
        }
        if(this.size == 1){
            const removedValue = this.head.value;
            this.size -= 1;
            this.head = null;
            return removedValue;
        }
        return this.removeNode(this.head)
    }
}

const stack = new Stack();
stack.push(3);
stack.push(5);
stack.push(8);
stack.push(2);
stack.print();
console.log(stack.length())
stack.pop();