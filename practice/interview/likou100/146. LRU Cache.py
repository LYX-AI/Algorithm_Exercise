'''
最终要实现的效果
put(1, 1) → 缓存：[(1,1)]
put(2, 2) → 缓存：[(1,1), (2,2)]（最新的在尾部）
get(1) → 返回 1，缓存变为：[(2,2), (1,1)]（因为 1 刚被使用，移到尾部）
put(3, 3) → 缓存已满，删除最久未使用的 2，插入 3：[(1,1), (3,3)]
get(2) → 返回 -1（键不存在）
put(4, 4) → 缓存已满，删除最久未使用的 1，插入 4：[(3,3), (4,4)]

'''

class DlinkNode:
    def __init__(self,key=0,value=0):
        self.key=key
        self.value=value
        self.prve=None
        self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.Cache={}
        self.capacity=capacity
        self.size=0

        self.dummy_head= DlinkNode()
        self.dummy_tail=DlinkNode()
        self.dummy_head.next=self.dummy_tail
        self.dummy_tail.prve=self.dummy_head
    def _add_to_tail(self,node:DlinkNode):
        node.next=self.dummy_tail
        node.prve=self.dummy_tail.prve
        self.dummy_tail.prve.next=node
        self.dummy_tail.prve=node
    def _remove_Node(self,node:DlinkNode):
        node.prve.next=node.next
        node.next.prve=node.prve
        node.next=None
        node.prve=None
    def _remove_to_tail(self,node:DlinkNode):
        self._remove_Node(node)
        self._add_to_tail(node)

    def _remove_head(self):
        node=self.dummy_head.next
        self._remove_Node(node)
        return node
    def get(self, key: int) -> int:
        if key not in self.Cache:
            return -1
        else:
            node=self.Cache[key]
            self._remove_to_tail(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.Cache:
            node=self.Cache[key]
            node.value=value
            self._remove_to_tail(node)
        else:
            node=DlinkNode(key,value)
            self.Cache[key]=node
            self._add_to_tail(node)
            self.size+=1
        if self.size>self.capacity:
            remove_node=self._remove_head()
            self.Cache.pop(remove_node.key)
            self.size-=1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)