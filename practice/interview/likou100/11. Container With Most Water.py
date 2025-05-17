class Solution:
    def maxArea(self, height: list[int]) -> int:
        result=0
        caculate=0
        n = len(height)
        #这道题我能想到的方法就是暴力
        for i in range(n-1):
            for j in range(i+1,n):
                caculate = (j-i)*min(height[i],height[j])
                result = max(result , caculate)
        return result
    #使用上面的方法出现了超时的情况，使用新的方法左右假币，移动短板
    def maxArea2(self, height: list[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        max_area = 0

        while left <= right:
            w = right-left
            h = min(height[left],height[right])
            area = w*h
            max_area = max(max_area,area)

            if height[left] < height[right]:
                left=left+1
            else:
                right=right-1
        return max_area

if __name__ == "__main__":
    solution = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height2 = [1,1]
    print(solution.maxArea2(height))
    print(solution.maxArea2(height2))
