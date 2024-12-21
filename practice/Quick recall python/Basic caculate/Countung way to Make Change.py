def countWay(coins,amount):
    dp=[0]*[amount+1]
    dp[0]=1
    for coin in coins:
       for x in range(coin,amount+1):
           dp[x]+=dp[x]+dp[x-coin]
    return dp[amount]

'''
动态规划最重要的思路就是从coins中拿出一个硬币，能组成当前面值的方法数量=当前面值默认的组成方法数+能组成（当前面值-拿出硬币的面值）的面值的组成方法
'''