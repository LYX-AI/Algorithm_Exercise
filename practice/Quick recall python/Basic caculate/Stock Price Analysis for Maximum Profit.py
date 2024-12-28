'''
股票买卖最佳时机：

题目描述：给定一个数组，它的第i个元素是一支给定股票第i天的价格。设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
实际应用：金融市场分析，算法交易系统。
'''
def MaxProfit(prices):
    max_profit = 0
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            max_profit+=prices[i]-prices[i-1]
    return max_profit
price=[7,1,5,3,6,4]
print(MaxProfit(price))
'''
Knowledge Points
Loops: Understanding how to use loops to iterate through an array or list.
Conditional Statements: Using if conditions to determine when to buy or sell the stock.
Array Indexing: Accessing elements in a list using their index.
Basic Arithmetic Operations: Performing subtraction to calculate profit.
Aggregation: Summing up values over a loop to get a total amount.
Algorithm Efficiency: The solution is efficient with a time complexity of O(n), where n is the number of days.
'''