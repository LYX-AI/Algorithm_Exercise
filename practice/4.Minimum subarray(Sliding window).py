'''
topic:
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

example:
示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。

示例 2：

输入：target = 4, nums = [1,4,4]
输出：1

示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0

'''
'''
Train of throught:
Violent Solution:
    1.we need tow "for loop", two pointers i and j
    2. the i point to the start of the new array ,and the j point to the end of the new array

 pseudo-code:  
    i=0
    result=INT32_MAX
    for(i=0;i<nums.size();i++){
        sum=0
        for(j=0:j<nums.size(),j++){
            sum+=nums[j]
            if(sum>=s):
                SubLength=j-1+1
                这里的result存储的是每次i不变（起始位置不变）的满足条件的结果
                result=reslut<SubLength ? result:SubLength
                break
        }
    return result==INT32_MAX ? 0:result
    }
'''


'''
Sliding window Solution(Double pointer Solution):
there are three things are very important to solve this question:
    1.which elements are in the sliding windows(between)?
        the sum of elements in is >= s;
    2.when to move the head pointer(the start of the window):
        when the sum of elements is >=s;
    3.when to move the end pointer(the end of the window)
        when the sum of elements in the widnow is <s

the import part:
        when to move the head pointer:
            while(sum>=s):
                SubLength=j-i+1;
                result=result<sublength ? result:sublength
                sum=sum-nums[i]
                i++
    
    the core code is this:
     while(sum>=target):
                Sublength=j-i+1
                result=min(result,Sublength)
                sum=sum-nums[i]
                i+=1
'''
#code
target=7
nums=[2,3,1,2,4,3]

class Solution:
#violent:
    def minSubArrayLen(target: int, nums: list[int]):
        l=len(nums)
        result=float('inf')
        for i in range(l):
            sum=0
            for j in range(i,l):
                sum+=nums[j]
                if sum>=target:
                    result=min(result,j-i+1)
                    break
        if result!=float('inf'):
            return result
        else:
            return 0


              
#Sliding window Solution(Double pointer Solution):

    def minSubArrayLen2(target: int, nums: list[int]):
        sum=0
        i=0
        result=float('inf')
        #这里for in range 是遍历从0 到len(nums)-1 是个左闭右开区间
        for j in range(0,len(nums)):
            sum=sum+nums[j]
            #什么时候前指针移动
            while(sum>=target):
                Sublength=j-i+1
                result=min(result,Sublength)
                sum=sum-nums[i]
                i+=1
        if(result!=float('inf')):
            return result
        else:
            return 0

print(Solution.minSubArrayLen2(target=target,nums=nums))