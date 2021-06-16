class ListNode:
    def __init__(self, key, value):
        self.previous = None
        self.next = None
        self.key = key
        self.value = value
    

class List:
    def __init__(self):
        self.node = ListNode(0,0)
        self.node.previous, self.node.next = self.node, self.node
    
    @property
    def head(self):
        return self.node.next
    
    @property
    def tail(self):
        return self.node.previous
    
    def remove(self, node):
        l, r = node.previous, node.next
        l.next, r.previous = r, l
    
    def insertToHead(self, node):
        l, r = self.node, self.node.next
        node.previous, node.next = l, r
        l.next, r.previous = node, node


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.list = List()

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.list.remove(node)
            self.list.insertToHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.list.remove(node)
            self.list.insertToHead(node)
        else:
            if len(self.cache) == self.capacity:
                del self.cache[self.list.tail.key]
                node = self.list.tail
                node.key, node.value = key, value
                self.list.remove(node)
            else:
                node = ListNode(key, value)
            self.cache[key] = node
            self.list.insertToHead(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)