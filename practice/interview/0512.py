def find_K_Number(nums,k):
    nums.sort(reverse=True)
    return nums[k-1]

if __name__ =="__main__":
    nums =[3,2,1,5,6,4]
    k=5
    print(find_K_Number(nums, k))