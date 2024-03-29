'''
topic:
    Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
'''
'''
solution1: Use dicutionaries
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]):
        table={}
        for num in nums1:
            table[num]=table.get(num,0)+1
        
        result=set()
        for num in nums2:
            if num in table:
                result.add(num)
                del table[num]

        return list(result)

'''
solution2: Use array
'''
def intersection2(self, nums1: List[int], nums2: List[int]):
    count1=[0]*1001
    count2=[0]*1001
    result=[]
    for i in range (len(nums1)):
        count1[nums1[i]]+=1
    for j in range (len(nums2)):
        count2[nums2[j]]+=1
    for k in range(1001):
        if count1[k]*count2[k]>0:
            result.append(k)
    return result
'''
solution3: use set 
'''
def intersection3(self, nums1: List[int], nums2: List[int]):
    return list(set(nums1)&set(nums2))