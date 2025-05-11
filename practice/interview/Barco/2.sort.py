def pop_sort(arr):
    n=len(arr)
    for i in range(n-1):
        sweep = False
        for j in range(n-j-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                sweep = True
        if sweep == False:
            break
    return arr

def sort_array(arr:list)->list:
    return sorted(arr)

print(sort_array([3,1,4,1,5,9]))