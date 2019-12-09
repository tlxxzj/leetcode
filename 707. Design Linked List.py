class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def print(self):
        node = self.head.next
        vals = []
        while node != self.tail:
            vals.append(node.val)
            node = node.next
        #print(vals)
    
    def insert(self, node, val):
        node2 = ListNode(val)
        node2.prev = node.prev
        node2.next = node
        node.prev.next = node2
        node.prev = node2
        self.size += 1
        #self.print()
    
    
    def remove(self, node):
        if not node:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        self.print()
    
    
    def get_node(self, index):
        if index < 0 or index >= self.size:
            return None
        node = self.head.next
        while index > 0:
            index -= 1
            node = node.next
        return node
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        return self.get_node(index).val
        
        
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.insert(self.head.next, val)
        
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.insert(self.tail, val)
        
        
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return
        if index == self.size:
            self.insert(self.tail, val)
            return
        node = self.get_node(index)
        self.insert(node, val)
        
            
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index <0 or index >= self.size:
            return
        node = self.get_node(index)
        self.remove(node)
        
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)