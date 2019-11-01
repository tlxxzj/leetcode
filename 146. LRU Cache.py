class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    
    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    
    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if node:
            self.remove_node(node)
            self.add_to_head(node)
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove_node(node)
            self.add_to_head(node)
            return
        elif len(self.cache) < self.capacity:
            node = Node(key, value)
            self.cache[key] = node
            self.add_to_head(node)
            return
        else:
            node = self.tail.prev
            del self.cache[node.key]
            node.key = key
            node.value = value
            self.cache[key] = node
            self.remove_node(node)
            self.add_to_head(node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)