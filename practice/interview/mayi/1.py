'''
这里有 n 堆竹子，第 i 堆中有 piles[i] 根竹子。饲养员已经离开了，将在 h 小时后回来。
花花可以决定她吃竹子的速度 k （单位：根/小时）。
每个小时，她将会选择一堆竹子，从中吃掉 k 根。如果这堆竹子少于 k 根，她将吃掉这堆的所有竹子，然后这一小时内不会再吃更多的竹子。
花花喜欢慢慢吃，但仍然想在饲养员回来前吃掉所有的竹子。
返回她可以在 h 小时内吃掉所有竹子的最小速度 k（k 为整数）。实例：输入：piles = [3,6,7,11], h = 8
输出：4 用python写
'''
import math


def min_eating_speed(piles, h):
    # 定义二分查找的左边界和右边界
    left, right = 1, max(piles)

    def can_finish(k):
        # 计算以速度 k 吃，是否能在 h 小时内吃完
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)
        return hours <= h

    # 二分查找
    while left < right:
        mid = (left + right) // 2
        if can_finish(mid):
            right = mid  # 尝试更慢的速度
        else:
            left = mid + 1  # 速度太慢，尝试更快的

    return left


# 示例
piles = [3, 6, 7, 11]
h = 8
print(min_eating_speed(piles, h))  # 输出：4
