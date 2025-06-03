class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            The_last = nums.pop()
            nums.insert(0,The_last)
        return nums
if __name__ == "__main__":
    soltion = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k =3
    print(soltion.rotate(nums,k))
