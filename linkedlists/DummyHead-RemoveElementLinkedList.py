from typing import Optional

"""
Problem: Remove Linked List Elements
https://leetcode.cn/problems/remove-linked-list-elements/
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Input: head = [], val = 1
Output: []

Input: head = [7,7,7,7], val = 7
Output: []
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My first-try version, not as elegant as the official one. But this is still O(n) time complexity.
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None: return head
        # deal with heading nodes being val
        while True:
            if head == None:
                return head
            if head.val == val:
                head = head.next
            else:
                break
        # now the head is head, set current. now current must not being 'val'
        current = head.next
        previous = head # placeholder
        while True:
            if current == None:
                break
            if current.val == val:
                previous.next = current.next
            else:
                previous = previous.next
            current = current.next
            
        return head
    
    
# Yeah, I know this one is better, my first-try version is not as elegant as this one.
class OfficialDummyHeadSolution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 创建虚拟头部节点以简化删除过程
        dummy_head = ListNode(next = head)
        
        # 遍历列表并删除值为val的节点
        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy_head.next

# Test cases
def test_solution():
    # Test case 1: Remove 6 from [1,2,6,3,4,5,6]
    # Create linked list: 1->2->6->3->4->5->6
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(6)
    head1.next.next.next = ListNode(3)
    head1.next.next.next.next = ListNode(4)
    head1.next.next.next.next.next = ListNode(5)
    head1.next.next.next.next.next.next = ListNode(6)
    
    # Expected result: 1->2->3->4->5
    sol = Solution()
    result1 = sol.removeElements(head1, 6)
    
    # Print result
    print("Test Case 1:")
    print_list(result1)  # Should be [1,2,3,4,5]
    
    # Test case 2: Remove 7 from [7,7,7,7]
    head2 = ListNode(7)
    head2.next = ListNode(7)
    head2.next.next = ListNode(7)
    head2.next.next.next = ListNode(7)
    
    # Expected result: []
    result2 = sol.removeElements(head2, 7)
    
    print("Test Case 2:")
    print_list(result2)  # Should be []
    
    # Test case 3: Remove 1 from []
    # Expected result: []
    result3 = sol.removeElements(None, 1)
    
    print("Test Case 3:")
    print_list(result3)  # Should be []

def print_list(head):
    """Helper function to print a linked list"""
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print("[" + ",".join(values) + "]" if values else "[]")

# Run the tests
if __name__ == "__main__":
    test_solution()

