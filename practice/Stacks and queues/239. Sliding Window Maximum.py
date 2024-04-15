'''
ou are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''
'''
Main thoght of this
if there are three function 
1.pop()
  when the window slide we need to remove the element and push the new
2.push ()
  after reomve the elements then we need to push the new elements in the queue
3.front()
    find the largest elements in the queue
the only thing we need to pay attention is that the largest element 
the largest elements should be the leftest in the queue
'''
from collections import deque
class Myque:
    def __init__(self) -> None:
        self.queue=deque()
    def pop(self,value):
        if self.queue and value==self.queue[0]:
            self.queue.popleft()
    def push(self,value):
        while  self.queue and value>self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)
    def front(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que=Myque()
        result=[]
        for i in range(k):
            que.push(nums[i])
        result.append(que.front())
        for i in range(k,len(nums)):
            que.pop(nums[i-k])
            que.push(nums[i])
            result.append(que.front())
        return result
           
