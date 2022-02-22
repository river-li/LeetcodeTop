#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
class LinkNode:
    def __init__(self) -> None:
        self.val = None
        self.key = None
        self.next = None
        self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.head = LinkNode()
        self.tail = LinkNode()
        self.cache = dict()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = LinkNode()
            node.val = value
            node.key = key
            self.cache[key] = node
            # 插入到头
            self.addNodeToHead(node)
            self.size = self.size + 1
            if self.size > self.capacity:
                # 移除尾部的节点
                removed = self.removeTail()
                # 注意删掉之后需要从缓存把key清除掉
                self.cache.pop(removed.key)
                self.size = self.size -1
        else:
            node = self.cache[key]
            node.val = value
            self.moveToHead(node)

    
    def addNodeToHead(self, node: LinkNode):
        node.next = self.head.next
        node.prev = self.head
        # 这里有讲究的，下面这两个顺序不能变，做题时傻了debug半天
        self.head.next.prev = node
        self.head.next = node


    def removeNode(self, node: LinkNode):
        node.next.prev = node.prev
        node.prev.next = node.next

    def moveToHead(self, node: LinkNode):
        self.removeNode(node)
        self.addNodeToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

