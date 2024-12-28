'''
找零钱的方法数：

题目描述：给定不同面额的硬币和一个总金额。写一个函数来计算可以凑成总金额的硬币组合数。每种硬币的数量是无限的。
实际应用：自动售货机软件，金融软件系统。
'''
def countWay(coins,amount):
    dp=[0]*[amount+1]
    dp[0]=1
    for coin in coins:
       for x in range(coin,amount+1):
           dp[x]+=dp[x]+dp[x-coin]
    return dp[amount]

'''
动态规划最重要的思路就是从coins中拿出一个硬币，能组成当前面值的方法数量=当前面值默认的组成方法数+能组成（当前面值-拿出硬币的面值）的面值的组成方法
Dynamic Programming: This problem is a textbook example of dynamic programming where you build up a solution using previously computed values.
Array Manipulation: Using an array to store the number of ways to make each amount from 0 up to the total.
Looping Structures: Nested loops where the outer loop iterates over each coin and the inner loop updates the ways to make each amount.
Looping Structures: Nested loops where the outer loop iterates over each coin and the inner loop updates the ways to make each amount.
Initialization of Base Cases: Initializing the DP array such that dp[0] = 1 since there's only one way to make zero amount (no coins).
Understanding of Combinatorics: The problem involves combining items (coins) in different ways to achieve a target sum, requiring a clear understanding of combinations.

'''