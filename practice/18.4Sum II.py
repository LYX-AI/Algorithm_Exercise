'''
tiltle:
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

    0 <= i, j, k, l < n
    nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

'''
'''
Train of thought:
 there are four arrays ,and we can call them  A B C D
 we first traverse the A abd B to find the elements a in A find elements b in B
 1.we can element a+b;
 2.define a Hash table ,this part we chose to use map(because we can store two elemts in the map)
 3.use the a+b as the key and the how many a+b in the A and B is as the vlan of the a+b
 4.traverse the C and D and find the value target c+b which is sutisfied with tartget(c+d)=0-(a+b) 
and the result is count+ map[a+b]
'''
from collections import defaultdict

class Solution:
    def fourSumCount(nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]):
        record=dict()
        count=0
        for a in nums1:
            for b in nums2:
                if a+b not in record:
                    record[a+b]=0
                record[a+b]+=1
        for c in nums3:
            for d in nums4:
                target=0-(c+d)
                if target in record:
                    count+=record[target]
        return count
    def fourSumCount2(nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]):
        rec,cnt=defaultdict(lambda:0),0
        for a in nums1:
            for b in nums2:
                rec[a+b]+=1
        for c in nums3:
            for d in nums4:
                cnt+=rec.get(0-(c+d),0)
        return cnt   

nums1=[1,2]
nums2=[-2,-1]
nums3=[-1,2]
nums4=[0,2]

print(Solution.fourSumCount(nums1,nums2,nums3,nums4))
