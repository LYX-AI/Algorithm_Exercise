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
