class Node {
    constructor(value) {
        this.value = value;
        this.nextNode = null
    }

    getValue() {
        return this.value;
    }

    getNextNode() {
        return this.nextNode;
    }
}

class MyList {
    constructor() {
        this.firstNode = null;
    }

    isEmpty() {
        return (this.firstNode == null)
    }

    recursiveInsert(firstNode, newNode) {
        if (firstNode.nextNode == null) {
            firstNode.nextNode = newNode;
        } else {
            this.recursiveInsert(firstNode.nextNode, newNode)
        }
    }

    insert(value) {
        const newNode = new Node(value);
        if (this.isEmpty())
            this.firstNode = newNode;
        else {
            this.recursiveInsert(this.firstNode, newNode)
        }
    }

    recursivePrint(node) {
        if (node == null) return;
        console.log(node.value);
        this.recursivePrint(node.nextNode)
    }

    print() {
        if (this.firstNode == null) { console.log("[]"); return; };
        this.recursivePrint(this.firstNode)
    }

    recursivePrintAll(node, values) {
        if (node == null) {
            console.log(values);
            return values;
        }
        values.push(node.value);
        return this.recursivePrintAll(node.nextNode, values);
    }

    printAll() {
        const values = []
        if (this.isEmpty()) { console.log(values); return values };
        return this.recursivePrintAll(this.firstNode, values);
    }

    recursiveSize(firstNode, count) {
        count += 1;
        if (firstNode.nextNode == null) {
            return count;
        }
        return this.recursiveSize(firstNode.nextNode, count);
    }

    size() {
        let count = 0;
        if (this.isEmpty()) {
            return count;
        }
        return (this.recursiveSize(this.firstNode, count));
    }

    recursiveExist(firstNode, value) {
        if (firstNode.getValue() == value) {
            return true;
        } else if (firstNode.getNextNode() == null) {
            return false;
        }
        return this.recursiveExist(firstNode.getNextNode(), value);
    }

    exist(value) {
        if (this.isEmpty()) {
            return false;
        }
        return this.recursiveExist(this.firstNode, value);
    }

    recursiveIndexOf(node, value, index) {
        if (node.value == value) {
            return index;
        }
        index++
        return this.recursiveIndexOf(node.nextNode, value, index);
    }

    indexOf(value) {
        if (!this.exist(value)) {
            return undefined;
        }
        return this.recursiveIndexOf(this.firstNode, value, 0);
    }

    recursivePop(currentNode) {
        if (currentNode.nextNode.nextNode == null) {
            const numRemoved = currentNode.nextNode.value;
            currentNode.nextNode = null
            return numRemoved;
        }
        return this.recursivePop(currentNode.nextNode)
    }

    pop() {
        if (this.isEmpty()) return undefined;
        if (this.size() == 1) {
            const value = this.firstNode.value
            this.firstNode = null
            return value;
        }
        return this.recursivePop(this.firstNode);
    }

    recursiveRemove(node, value) {
        if (node.nextNode.value == value) {
            node.nextNode = node.nextNode.nextNode;
            return;
        }
        return this.recursiveRemove(node.nextNode, value);
    }

    removeValue(value) {
        if (!this.exist(value)) { console.log(undefined); return undefined };
        if(this.firstNode.value == value){
            this.firstNode = this.firstNode.nextNode;
            return;
        }
        return this.recursiveRemove(this.firstNode, value);
    }

    recursiveRemoveByIndex(node, index, count){
        if(index -1 == count){
            let founded = node.nextNode;
            node.nextNode = node.nextNode.nextNode;
            return founded.value;
        }
        count += 1
        return this.recursiveRemoveByIndex(node.nextNode, index, count);
    }

    removeByIndex(index){
        if(index == 0){
            const founded = this.firstNode.value;
            this.firstNode = this.firstNode.nextNode;
            return founded;
        }
        if(this.size() > index){
            return this.recursiveRemoveByIndex(this.firstNode, index, 0)
        }
        return undefined;
    }

    recursiveFind(currentNode, index, count){
        if(index == count){
            return currentNode.value;
        }
        count++
        return this.recursiveFind(currentNode.nextNode, index, count)
    }

    findByIndex(index){
        if(this.size() > index){
            return this.recursiveFind(this.firstNode, index, 0);
        }
        return undefined;
    }

    recursiveSum(node, sum) {
        if (node == null) {
            return sum;
        }
        sum += node.value;
        return this.recursiveSum(node.nextNode, sum)
    }

    sum() {
        let sum = 0
        if (this.isEmpty()) { console, log(null); return null; }
        return this.recursiveSum(this.firstNode, sum);
    }

    recursiveSort(node, flag) {
        if (node.nextNode == null) {
            return flag;
        }
        if (node.value > node.nextNode.value) {
            let maxCurrentValue = node.value;
            node.value = node.nextNode.value;
            node.nextNode.value = maxCurrentValue;
            flag = true;
        }
        return this.recursiveSort(node.nextNode, flag)
    }

    sort() {
        if (this.isEmpty()) { console.log(null); return null; }
        while (this.recursiveSort(this.firstNode, false)) { }
        return this.printAll();
    }

    recursiveReverse(node, previous){
        if(node == null){
            return this.firstNode = previous;
        }
        let next = node.nextNode;
        node.nextNode = previous;
        previous = node;
        return this.recursiveReverse(next, previous);
    }

    reverse(){
        if(this.isEmpty()) return undefined;
        return this.recursiveReverse(this.firstNode, null);
    }

    recursiveConcat(node, newList){
        if(node.nextNode == null){
            node.nextNode = newList.firstNode;
            return node;
        }
        return this.recursiveConcat(node.nextNode, newList);
    }

    concat(newList){
        if(this.isEmpty()) return newList;
        this.recursiveConcat(this.firstNode, newList);
    }
}

const list = new MyList();
console.log("SIZE:");
console.log(list.size());
list.insert(2);
list.insert(1);
list.insert(3);
list.insert(0);
console.log("\nPRINT:");
list.printAll();
console.log("\nSORT:");
list.sort();
list.removeValue(2);
console.log("\nPRINT AFTER REMOVE 2:");
list.printAll();
console.log("\nSUM:");
console.log(list.sum());
console.log("\nIS EMPTY ?");
console.log(list.isEmpty());
console.log("\nEXIST 2 ?");
console.log(list.exist(2));
console.log("\nSIZE:");
console.log(list.size());
console.log("\nINDEX OF 3:");
console.log(list.indexOf(3));
console.log("\nPOP:");
console.log(list.pop());
console.log("\nPRINT:");
list.print();
list.insert(7);
list.insert(3);
list.insert(2);
list.insert(8);
console.log("\nPRINT AFTER NEW INSERTIONS:");
list.printAll();
console.log("\nFIND BY INDEX 2:");
console.log(list.findByIndex(2));
console.log("\nREMOVE BY INDEX 0:");
console.log(list.removeByIndex(0));
console.log("\nPRINT AFTER REMOVE AT INDEX 0:");
list.printAll();
console.log("\nREMOVE BY INDEX 3:");
console.log(list.removeByIndex(3));
console.log("\nPRINT AFTER REMOVE AT INDEX 3:");
list.printAll();
console.log("\nREVERSE:");
list.reverse();
list.printAll();
const newList = new MyList();
newList.insert(2);
newList.insert(5);
newList.insert(9);
console.log("\nPRINT NEW LIST:");
newList.printAll();
console.log("\nCONCAT LISTS:");
list.concat(newList);
list.printAll();