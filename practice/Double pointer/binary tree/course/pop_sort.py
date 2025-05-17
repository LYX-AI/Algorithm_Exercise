def pop_sort(nums):
    n=len(nums)
    for i in range(n-1):
        sweep = False
        for j in range(n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                sweep = True
        if not sweep:
            break
    return nums

if __name__ == "__main__":
    nums=[2,8,7,9,1,0,10]
    print(pop_sort(nums))