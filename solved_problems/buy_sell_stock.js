// You are given an array prices where prices[i] is the price of a given stock on the ith day.

// You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

// Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

// Example 1:
// Input: prices = [7,1,5,3,6,4]
// Output: 5
// Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
// Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

// Example 2:
// Input: prices = [7,6,4,3,1]
// Output: 0
// Explanation: In this case, no transactions are done and the max profit = 0.

// Constraints:
// 1 <= prices.length <= 105
// 0 <= prices[i] <= 104

function maxProfit (prices) {
    let buy = 0
    let sale = 1
    let priceBuy = 0
    let priceSale = 0
    let profit = 0
    while(sale < prices.length){
        if(prices[buy] < priceBuy){ 
            priceBuy = prices[buy]
        }
        if(prices[sale] > priceSale){
            priceSale = prices[sale]
        }
        if(prices[sale] < prices[buy]){
            buy = sale
        }
        if(priceBuy < priceSale){ 
            priceBuy = prices[buy]
            priceSale = prices[sale]
            let currentProfit = priceSale - priceBuy
            if(currentProfit > profit)
                profit = currentProfit
        }
        sale += 1
    }
    return profit;
};

let prices = [4,2,1,7]
console.log(maxProfit(prices))
prices = [8,6,4,3,3,2,3,5,8,3,8,2,6]
console.log(maxProfit(prices))
prices = [7, 1, 5, 3, 6, 4]
console.log(maxProfit(prices))
prices = [7,6,4,3,1]
console.log(maxProfit(prices))
prices = [1, 4, 1, 4, 3, 1]
console.log(maxProfit(prices))


