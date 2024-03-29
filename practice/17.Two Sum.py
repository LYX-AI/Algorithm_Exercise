'''
Topic:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
'''
example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
'''
Train of thought:
we need an map to store the elemnts of the array and traverse the array to find the elements + the one has already sotre in the map = target value


 There are four questions we need to make clear to follow this questioon
    1.Why we use Hash to store the number:
        This subject need us to traverse the array, and store the elements in it, when we need to find the
        this element we need find an elements in this set ,so the first thing  we need to think about hash table 
    
    2.Why we chose map as the Hash 
        Because we not only need to know whether the values of these elements but also need to know the subscript of the elements
        so we need to store two values 1.elements and 2.values so we chose map

    3. what the useful of the map
        Used to store the elements and the values of the elements
    
    4.What is key and what is value in the map
        the goal of us is to find whether the elements in the array has ever appeared
        so the value of the elemet should be the key of the map and the subscript of the elements should be the value of the map

        so we can have a conclusion of the map(key: the value of the element,  value:the subscript of the element)

'''
#This is a mistake in the subject is not an array is a list
'''
列表（List）：

    列表是Python中的内置数据类型，非常灵活，可以容纳不同类型的元素，包括整数、字符串、对象等。
    列表的长度可以动态变化，您可以随时添加或删除元素。
    列表使用方括号 [] 来定义，元素之间用逗号 , 分隔。
    列表的索引从0开始。

示例：

python

my_list = [1, 2, 3, "hello", [4, 5]]

数组（Array）：

    数组通常指的是NumPy库（Numeric Python）中的数组。NumPy是一个Python库，用于数值计算，它提供了多维数组对象。
    NumPy数组中的元素通常是同一种数据类型，例如，都是整数或浮点数。
    数组的长度通常是固定的，一旦创建，它的大小通常不会改变。
    数组支持高效的数学和科学计算操作，例如矩阵运算、统计计算等。

示例（使用NumPy创建数组）：

python

import numpy as np

my_array = np.array([1, 2, 3, 4, 5])

总的来说，如果您需要一个通用的、灵活的数据结构，可以容纳不同类型的元素并支持动态大小的操作，那么列表是一个不错的选择。如果您进行数学或科学计算，并且需要处理大量的数值数据，那么使用NumPy数组可能更加高效和方便。选择使用哪种数据结构取决于您的具体需求。
'''

# in the python we have directory like the map
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int):
        record=dict()
        for index ,val in enumerate(nums):
            if target-val in record:
                return [record[target-val],index]
            record[val]=index
        return []

# We can also us set to store the elements
    def twoSum2(self, nums: List[int], target: int):
        record=set()
        for index,val in enumerate(nums):
            temp=target-val
            if temp in record:
                return [index,nums.index(temp)]
            record.add(val)
#violent
    def twoSum3(self, nums: List[int], target: int):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]
        return []
'''
以上方法一和方法二分别使用map和set来存储
区别是
map[key:目标的值，val：目标的下标]
set[遍历过的元素值]
'''
'''
double pointer 这个方法有点绕我认为可以先放放

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 对输入列表进行排序
        nums_sorted = sorted(nums)
        
        # 使用双指针
        left = 0
        right = len(nums_sorted) - 1
        while left < right:
            current_sum = nums_sorted[left] + nums_sorted[right]
            if current_sum == target:
                # 如果和等于目标数，则返回两个数的下标
                left_index = nums.index(nums_sorted[left])
                right_index = nums.index(nums_sorted[right])
                if left_index == right_index:
                    right_index = nums[left_index+1:].index(nums_sorted[right]) + left_index + 1
                return [left_index, right_index]
            elif current_sum < target:
                # 如果总和小于目标，则将左侧指针向右移动
                left += 1
            else:
                # 如果总和大于目标值，则将右指针向左移动
                right -= 1
'''
这里有个知识点可以学习下

nums.index(nums_sorted[left]) 返回的是第一次匹配的元素的索引，而不是随机返回一个值满足 nums_sorted[left] 的下标。
'''