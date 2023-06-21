// In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

// We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

// Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

// If it cannot be done, return -1.

// Example 1:
// Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
// Output: 2
// Explanation: 
// The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
// If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

// Example 2:
// Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
// Output: -1
// Explanation: 
// In this case, it is not possible to rotate the dominoes to make one row of values equal.

// Constraints:
// 2 <= tops.length <= 2 * 104
// bottoms.length == tops.length
// 1 <= tops[i], bottoms[i] <= 6


let tops = [2, 1, 2, 4, 2, 2]
let bottoms = [5, 2, 6, 2, 3, 2]
let allNumbers = tops.concat(bottoms);
let mid = Math.floor(allNumbers.length / 2)

var minDominoRotations = function (tops, bottoms) {

    if (tops.length != bottoms.length)
        return null;

    let allNumbers = tops.concat(bottoms);
    let mid = Math.floor(allNumbers.length / 2);
    let count = 0;
    let notPossible = false;
    let countEquals = 0;
    for (let i = 0; i < allNumbers.length / 2; i++) {
        if (allNumbers[i] != allNumbers[mid]) {
            if (allNumbers[i + 1] != allNumbers[i]) {
                if (allNumbers[mid + 1] == allNumbers[i]) {
                    let top = allNumbers[i + 1]
                    let bottom = allNumbers[mid + 1]
                    allNumbers[i + 1] = bottom
                    allNumbers[mid + 1] = top
                    count += 1
                }
            }
        } else {
            countEquals += 1;
        }
        mid++
    }
    let top = allNumbers.slice(0, tops.length)
    let bot = allNumbers.slice(tops.length)
    for (let i = 0; i < top.length - 1; i++) {
        if (top[i] != top[i + 1] && bot[i] != bot[i + 1])
            notPossible = true;
    }
    if (notPossible) {
        return -1
    }
    let dif = (allNumbers.length / 2) - countEquals;
    let comp = dif - count;
    if (comp < count)
        return comp;
    return count;
};

console.log(minDominoRotations(tops, bottoms))
