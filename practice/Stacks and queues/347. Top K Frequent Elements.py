'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1.获取每个元素出现的次数
        map_num={}
        for i in  nums:
            map_num[i]=map_num.get(i,0)+1
        #2.对value值进行排序，存在一个小根堆里
        pri_squ=[]
        for key,val in map_num.items():
            heapq.heappush(pri_squ,(val,key))
            if len(pri_squ)>k:
                heapq.heappop(pri_squ)
        #因为是小根堆，所以进行倒叙把结果输入到一个列表中
        result=[0]*k
        for i in range(k-1,-1,-1):
            reslue[i]=heapq.heappop(pri_squ)[1]
        return result
'''
在 Python 中，`heapq` 模块提供了一种简单的方式来实现和操作堆，也被称为优先队列。堆是一种特殊的完全二叉树，所有的节点都大于等于（最大堆）或小于等于（最小堆）它们的子节点。Python 的 `heapq` 模块实现了一个最小堆，即父节点的值总是小于或等于其子节点的值。

### `heapq.heappush(heap, item)`
- `heappush` 函数用于将一个元素添加到已存在的堆列表中，并保持堆的属性。这个过程包括将元素添加到列表的末尾，然后进行上浮操作（如果需要的话），以确保新加入的元素如果小于其父节点，则交换这两个元素的位置。这个过程可能会持续进行，直到添加的元素大于其父节点或者它已经是根元素。
- 这样做保证了堆的根节点总是最小元素。

### `heapq.heappop(heap)`
- `heappop` 函数用于移除并返回堆中最小的元素（堆顶元素）。移除堆顶元素后，`heapq` 将堆中的最后一个元素移动到根位置，然后执行下沉操作，即比较新的根节点与其子节点的值，如果根节点大于其子节点的值，它们将被交换。这个过程会重复，直到新的根节点小于其子节点，或者它已经是叶子节点。
- 通过这种方式，`heapq` 在每次弹出操作后都能保持最小堆的属性，确保根节点始终是最小的元素。

### 顺序示例
假设你有一个空的堆 `heap` 并进行以下操作：
```python
import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 9)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)
```
此时堆 `heap` 中的元素可能看起来像这样（虽然物理存储为数组，但逻辑上维护为最小堆）:
```
      1
    /   \
   3     9
  / \
 5   4
```
现在如果你执行 `heappop`：
```python
smallest = heapq.heappop(heap)
```
返回的 `smallest` 是 `1`，然后堆将重新调整为：
```
      3
    /   \
   4     9
  /
 5
```
堆始终保持最小的元素在顶部。这种数据结构特别适合需要快速访问最小元素但又频繁更新集合的场景。
'''