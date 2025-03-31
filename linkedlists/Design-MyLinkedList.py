"""
Problem: Design a Linked List
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.

Implement the MyLinkedList class:
- MyLinkedList() Initializes the MyLinkedList object.
- int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
- void addAtHead(int val) Add a node of value val before the first element of the linked list.
- void addAtTail(int val) Append a node of value val as the last element of the linked list.
- void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list.
- void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
"""

class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if self.head is None: return -1
        current = self.head
        for _ in range(index):
            current = current.next
            if current is None:
                return -1
        return current.val

    def printlist(self):
        if self.head is None: return
        current = self.head
        while current is not None:
            print(current.val, end=' ')
            current = current.next

    def addAtHead(self, val: int) -> None:
        if self.head is None: 
            self.head = ListNode(val)
            self.length = 1
            return
        self.length += 1
        new_head = ListNode(val, self.head)
        self.head = new_head
        # self.printlist()

    def addAtTail(self, val: int) -> None:
        if self.head is None: 
            self.head = ListNode(val)
            self.length = 1
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = ListNode(val)
        self.length += 1
        # self.printlist()

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.length:
            self.addAtTail(val)
            return
        if self.head is None: return
        current = self.head
        for i in range(index -1):
            current = current.next
            if current is None:
                return
        self.length += 1
        new_node = ListNode(val, current.next)
        current.next = new_node
        # self.printlist()

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None: return
        if index == 0: 
            self.length -= 1
            self.head = self.head.next
            return
        if index >= self.length: return
        current = self.head
        for _ in range(index -1):
            current = current.next
            if current is None:
                return
        self.length -= 1
        current.next = current.next.next
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# Test cases
def test_my_linked_list():
    # Initialize linked list
    linkedList = MyLinkedList()
    
    # Test addAtHead
    linkedList.addAtHead(1)
    linkedList.addAtHead(2)
    print("After adding 2,1 at head:", end=' ')
    linkedList.printlist()
    print()
    
    # Test addAtTail
    linkedList.addAtTail(3)
    print("After adding 3 at tail:", end=' ')
    linkedList.printlist()
    print()
    
    # Test addAtIndex
    linkedList.addAtIndex(1, 4)
    print("After adding 4 at index 1:", end=' ')
    linkedList.printlist()
    print()
    
    # Test get
    print("Value at index 1:", linkedList.get(1))  # Should print 4
    
    # Test deleteAtIndex
    linkedList.deleteAtIndex(1)
    print("After deleting index 1:", end=' ')
    linkedList.printlist()
    print()

if __name__ == "__main__":
    test_my_linked_list()