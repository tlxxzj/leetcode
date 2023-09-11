class MyLinkedList:
    class Node:
        def __init__(self, val=0, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self):
        self.length = 0
        self.head = self.Node(0)
        self.tail = self.Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        #print(self.toList())

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        
        node = self.head.next
        while index > 0:
            node = node.next
            index -= 1
        
        return node.val
            
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        
        node = self.Node(val)
        head = self.head
        for i in range(index):
            head = head.next
        
        node.prev = head
        node.next = head.next
        head.next.prev = node
        head.next = node

        self.length += 1
        #print(self.toList())
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        
        head = self.head.next
        for i in range(index):
            head = head.next
        
        prev, next = head.prev, head.next
        prev.next = next
        next.prev = prev

        self.length -= 1
        #print(self.toList())
    
    def toList(self):
        nodes = []
        node = self.head.next
        for i in range(self.length):
            nodes.append(node.val)
            node = node.next
        return nodes

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
