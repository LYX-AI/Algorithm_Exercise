class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        water = 0
        left_max = [0]*n
        right_max = [0]*n

        #先构建left_max 列表
        left_max[0] = height[0]
        for i in range(1,n):
            left_max[i] = max(left_max[i-1],height[i])

        #同样的方法来构造right_max 列表
        right_max[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            right_max[i] = max(right_max[i+1],height[i])


        for i in range(n):
            water += min(left_max[i],right_max[i]) - height[i]

        return water

    def trap2(self, height: list[int]) -> int:
        if not height:
            return 0
        n = len(height)
        water = 0
        left = 0
        right = n-1
        left_max = 0
        right_max = 0

        while left<right:
            if height[left] < height[right]:
                if height[left]>=left_max:
                    left_max = height[left]
                else:
                    water += left_max-height[left]
                left +=1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max-height[right]
                right -=1
        return water



if __name__ == "__main__":
    solution = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(solution.trap2(height))