def pop_sort(arr):
    n=len(arr)
    for i in range(arr-1):
        sweep = False
        for j in range(arr-i-1):
            if arr[j]>=arr[j+1]:
                arr[j],arr[j+1]==arr[j+1],arr[j]
                sweep=True
        if not sweep:
            break
    return arr


def quick_sort(arr):
    def _partition(high,low):
        piovt=arr[high]
        i=low-1
        for j in range(low,high):
            if arr[j]<=piovt:
                i+1
                arr[i],arr[j]=arr[j],arr[i]
        arr[i+1],arr[high]=arr[high],arr[i+1]
        return i+1
    def _quick_sor(low,high):
        if low<high:
            pi=_partition(high,low)
            _quick_sor(low,pi-1)
            _quick_sor(pi+1,high)
        _quick_sor(0,len(arr)-1)
        return arr



