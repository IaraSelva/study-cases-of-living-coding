// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Every close bracket has a corresponding open bracket of the same type.
 

// Example 1:
// Input: s = "()"
// Output: true

// Example 2:
// Input: s = "()[]{}"
// Output: true

// Example 3:
// Input: s = "(]"
// Output: false
 
// Constraints:

// 1 <= s.length <= 104
// s consists of parentheses only '()[]{}'.


var isValid = function(s) {
    const listOfChar = s.split('')
    const stack = new Stack();
    let isValid = true;

    listOfChar.forEach(char => {
        if(char == '(' || char == '[' || char == "{"){
            stack.push(char);
        }else{
            const lastInsert = stack.pop();
            if(!lastInsert){
                isValid = false;
            }
            if(lastInsert == '(' && char != ')'){

                isValid = false
            }
            if(lastInsert == '[' && char != ']'){
                isValid = false
            }
            if(lastInsert == '{' && char != '}'){
                isValid = false
            }
        }
    });
    return stack.size == 0 && isValid
};

class Node{
    constructor(value){
        this.value = value;
        this.nextNode = null;
    }
}

class Stack{
    constructor(){
        this.head = null;
        this.size = 0;
    }

    insertNodes(node, newNode){
        if(node.nextNode == null){
            this.size += 1;
            return node.nextNode = newNode;
        }
        return this.insertNodes(node.nextNode, newNode);
    }

    push(value){
        const newNode = new Node(value)
        if(this.head == null){
            this.head = newNode;
            this.size += 1;
            return newNode;
        }
        return this.insertNodes(this.head, newNode);
    }

    removeNodes(node){
        if(node.nextNode.nextNode == null){
            const removedValue = node.nextNode.value;
            this.size -= 1;
            node.nextNode = null;
            return removedValue;
        }
        return this.removeNodes(node.nextNode);
    }

    pop(){
        if(this.size == 0){
            return null;
        }
        if(this.size == 1){
            const removedValue = this.head.value;
            this.size -= 1;
            this.head = null;
            return removedValue;
        }
        return this.removeNodes(this.head);
    }
}

let string = "(([]){})"
console.log(isValid(string));
string = "("
console.log(isValid(string));
string = "()"
console.log(isValid(string));
string = "({{}})]"
console.log(isValid(string));
string = "{([])}"
console.log(isValid(string));
string = "[}"
console.log(isValid(string));

