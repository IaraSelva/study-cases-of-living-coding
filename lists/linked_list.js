class Node {
    constructor(valor) {
        this.valor = valor;
        this.proximoNo = null
    }

    getValor(){
        return this.valor;
    }

    getProximoNo(){
        return this.proximoNo;
    }
}

class Lista {
    constructor() {
        this.primeiroNo = null;
    }

    isEmpty() {
        if (this.primeiroNo == null)
            return true;
        return false;
    }

    recursiveInsert(primeiroNo, newNode) {
        if (primeiroNo.proximoNo == null) {
            primeiroNo.proximoNo = newNode;
        } else {
            this.recursiveInsert(primeiroNo.proximoNo, newNode)
        }
    }

    insert(value) {
        const newNode = new Node(value);
        if (this.isEmpty())
            this.primeiroNo = newNode;
        else {
            this.recursiveInsert(this.primeiroNo, newNode)
        }
    }

    recursivePrint(primeiroNo) {
        if (primeiroNo.proximoNo != null) {
            console.log(primeiroNo.proximoNo.valor)
            this.recursivePrint(primeiroNo.proximoNo)
        }
    }

    print() {
        if (this.isEmpty()) {
            console.log('lista vazia - usar o metodo insert()')
            return;
        }
        if (this.primeiroNo.proximoNo == null) {
            console.log(this.primeiroNo.valor);
        } else {
            console.log(this.primeiroNo.valor);
            this.recursivePrint(this.primeiroNo);
        }
    }

    recursiveSize(primeiroNo, count){
        count += 1;
        if(primeiroNo.proximoNo != null){
            return this.recursiveSize(primeiroNo.proximoNo, count);
        }
        return count;
    }

    size() {
        let count = 0;
        if (this.isEmpty()) {
            console.log(count);
            return;
        }
        console.log(this.recursiveSize(this.primeiroNo, count));
    }

    recursiveExist(primeiroNo, valor){
        if(primeiroNo.getValor() == valor){
            return true;
        }
        if(primeiroNo.getProximoNo() != null){
            return this.recursiveExist(primeiroNo.getProximoNo(), valor);
        }
        return false;
    }

    exist(valor){
        if(this.isEmpty()){
            return false;
        }
        return this.recursiveExist(this.primeiroNo, valor);
    }
}

const lista = new Lista();
console.log(lista.exist(3));
lista.insert(1);
lista.insert(2);
lista.insert(5);
lista.insert(7);
lista.insert(9);
lista.insert(3);
