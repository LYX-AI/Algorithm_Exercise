
class Solution:
    #[]
    def Dichotomy_search(self,nums:list[int], target:int):
        left=0
        right=len(nums)-1
        while(left<right or left==right):
            middle=left+(right-left)%2
            if nums[middle]<target:
                left=middle+1
            elif nums[middle]>target:
                right=middle-1
            else:
                return middle
        return -1
    #[)
    def Dichotomy_search2(nums:list[int],target:int):
        left=0
        right=len(nums)
        while(left<right):
            middle=left+(right-left)%2
            if(nums[middle]<target):
                left=middle+1 
            elif(nums[middle>target]):
                right=middle
            else:
                return middle
        return -1


print(Solution.Dichotomy_search(nums=[1,4,6,8,10],target=10))