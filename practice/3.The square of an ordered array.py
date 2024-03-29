'''
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
示例 1：
	• 输入：nums = [-4,-1,0,3,10]
	• 输出：[0,1,9,16,100]
	• 解释：平方后，数组变为 [16,1,0,9,100]，排序后，数组变为 [0,1,9,16,100]
示例 2：
	• 输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]
'''
'''
The most important thing is that, in the array the Maximum value of the square must in the edge of the array
so we define two pointer from two side of the arrary to ergodic the array while i<=j
'''
#Python中的列表实际上是动态数组的一种实现，因此在Python中使用列表往往能满足大多数需求。
nums = [-4,-1,0,3,10]
class Solution:
    def sortedSquares(nums: list[int]):
        i,j,r=0,len(nums)-1,len(nums)-1
#这行代码创建了一个名为res的列表，列表的长度与nums列表相同，每个元素初始化为正无穷大（float('inf')）。
        res=[float('inf')]*len(nums)
        while i<=j:
            if(nums[i]**2>nums[j]**2):
                res[r]=nums[i]**2
                r-=1
                i+=1
            else:
                res[r]=nums[j]**2
                r-=1
                j-=1
        return res


#viloent solution
    def sortedSquares2(nums: list[int]):
        #range(len(nums))：range() 函数生成一个包含从 0 到 len(nums) - 1 的整数序列，用于循环遍历列表 nums 中的元素。
        for i in range(len(nums)):
            nums[i]=nums[i]**2
        nums.sort()
        return nums
print(Solution.sortedSquares2(nums))

