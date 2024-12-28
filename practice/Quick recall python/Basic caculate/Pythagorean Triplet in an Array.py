'''
Pythagorean Triplet：

题目描述：编写一个函数，找出数组中是否存在三个数a，b，c，满足a² + b² = c²。
实际应用：数学问题解决，算法设计
'''
def checkTriplet(arr):
    n=len(arr)
    for i in range(n):
        arr[i]=arr[i]**2

    arr.sort()
    for i in range(n-1,1,-1):
        left=0
        right=i-1
        while left<right:
            if arr[i]==arr[left]+arr[right]:
                return True
            elif arr[i]>arr[left]+arr[right]:
                left+=1
            else:
                right-=1
        return False
    '''
    Knowledge Points:
    Array Manipulation: Squaring each element and sorting the array.
    Two-pointer Technique: Using two pointers to find two numbers that add up to the square of the third number.
    Sorting: Sorting the array to make the two-pointer technique applicable.
    Loops: Using nested loops effectively to iterate through array elements.
    Conditional Logic: Implementing conditions to compare the sum of squares to other elements.
    Optimization: Understanding how sorting and two-pointer approach reduce the time complexity compared to a naive approach.
    '''
