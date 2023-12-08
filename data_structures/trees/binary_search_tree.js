class Node {
    constructor(value) {
        this.value = value;
        this.leftNode = null;
        this.rightNode = null;
    }

    height() {
        if (this.leftNode == null && this.rightNode == null) {
            return 0
        }
        const leftHeight = this.leftNode ? this.leftNode.height() : null
        const rightHeight = this.rightNode ? this.rightNode.height() : null
        if (leftHeight > rightHeight) {
            return leftHeight + 1
        } else {
            return rightHeight + 1
        }
    }
}

class Tree {
    constructor() {
        this.root = null;
    }

    recursiveInsert(node, newNode) {
        if (node.value < newNode.value) {
            if (node.rightNode == null) {
                return node.rightNode = newNode;
            }
            return this.recursiveInsert(node.rightNode, newNode)
        }
        else {
            if (node.leftNode == null) {
                return node.leftNode = newNode
            }
            return this.recursiveInsert(node.leftNode, newNode)
        }
    }

    insertValue(value) {
        const newNode = new Node(value)
        if (this.root == null) {
            return this.root = newNode
        }
        return this.recursiveInsert(this.root, newNode)
    }

    exist(value, node = this.root) {
        if (node == null) {
            return false
        }
        if (node.value == value) {
            return true
        }
        if (node.value < value) {
            return this.exist(value, node.rightNode)
        } else {
            return this.exist(value, node.leftNode)
        }
    }

    print(node = this.root) {
        if (node.leftNode != null) { this.print(node.leftNode) }
        console.log(node.value)
        if (node.rightNode != null) { this.print(node.rightNode) }
    }

    height() {
        return this.root.height()
    }

    reverseTree(node = this.root) {
        if (node.leftNode != null) { this.reverseTree(node.leftNode) }
        if (node.rightNode != null) { this.reverseTree(node.rightNode) }
        let nodeAux = node.leftNode
        node.leftNode = node.rightNode
        node.rightNode = nodeAux
    }

    findMinValue(node) {
        if (!node.leftNode) { return node.value }
        return this.findMinValue(node.leftNode)
    }

    findMaxValue(node) {
        if (!node.rightNode) { return node.value }
        return this.findMaxValue(node.rightNode)
    }

    removeNode(value, node) {
        if (node == null) {
            return node;
        }

        if (node.value < value) {
            node.rightNode = this.removeNode(value, node.rightNode)
        }
        else if (node.value > value) {
            node.leftNode = this.removeNode(value, node.leftNode)
        }

        else {

            if (!node.leftNode && !node.rightNode) {
                return node = null
            }
            if (!node.leftNode) {
                return node.rightNode
            }
            else if (!node.rightNode) {
                return node.leftNode
            }

            node.value = this.findMinValue(node.rightNode)
            node.rightNode = this.removeNode(node.value, node.rightNode)

        }
        return node
    }

    removeValue(value) {
        this.root = this.removeNode(value, this.root)
    }
}


const myTree = new Tree();
myTree.insertValue(9)
myTree.insertValue(13)
myTree.insertValue(7)
myTree.insertValue(5)
myTree.insertValue(2)
myTree.insertValue(1)
myTree.insertValue(15)
myTree.insertValue(21)
console.log("Tree")
myTree.print()
//           9
//         /   \
//        7     13
//       /       \
//       5       15
//      /         \
//     2          21
//    /
//   1

myTree.print()
console.log(`Min value = ${myTree.findMinValue(myTree.root)}`)
console.log(`Max value = ${myTree.findMaxValue(myTree.root)}`)

console.log("Tree after delete leaf node")
myTree.removeValue(21)
myTree.print()

console.log("Tree after delete root node")
myTree.removeValue(9)
myTree.print()

//myTree.reverseTree()
//console.log("Reversed Tree")
console.log(JSON.stringify(myTree))
