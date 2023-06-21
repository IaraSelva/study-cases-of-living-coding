const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
let index;

function findTarget(numbers, target, index = 0) {
    let middle = Math.floor(numbers.length / 2)
    for (number in numbers) {
        if(numbers.length == 1 && number != target) return false;
        if (numbers[middle] == target)
            return index + middle;
        if (numbers[middle] < target) {
            return findTarget(numbers.slice(middle, numbers.length), target, middle+index);
        }
        else if (numbers[middle] > target) {
            return findTarget(numbers.slice(0, middle), target, index)
        }
        return false;
    }
}

console.log(findTarget(numbers, 0));
console.log(findTarget(numbers, 1));
console.log(findTarget(numbers, 2));
console.log(findTarget(numbers, 3));
console.log(findTarget(numbers, 4));
console.log(findTarget(numbers, 5));
console.log(findTarget(numbers, 6));
console.log(findTarget(numbers, 7));
console.log(findTarget(numbers, 8));
console.log(findTarget(numbers, 9));
console.log(findTarget(numbers, 10));
console.log(findTarget(numbers, 11));
console.log(findTarget(numbers, 12));

console.log(findTarget(numbers, 13));
console.log(findTarget(numbers, 20));
console.log(findTarget(numbers, 30));

