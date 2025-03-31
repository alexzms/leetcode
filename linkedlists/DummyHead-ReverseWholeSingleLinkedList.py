"""
Problem: Reverse a singly linked list
https://leetcode.cn/problems/reverse-linked-list/
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Solution Approach (Dummy Head):
Using a dummy head node to simplify the reversal process:
1. Create a dummy head node with value 0
2. For each current node:
   - Store the next node temporarily
   - Make current node point to dummy head's next
   - Make dummy head point to current node
   - Move current to the stored next node
3. Return dummy head's next (which is the new head)

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(1) as we only use a constant amount of extra space
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SolutionDummyHead:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0, None)
        cur = head
        while cur is not None:
            tmp = cur.next
            cur.next = dummy_head.next
            dummy_head.next = cur
            cur = tmp
        return dummy_head.next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sol = SolutionDummyHead()
        return sol.reverseList(head)

# Test cases
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linkedListToArray(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_reverseList():
    solution = Solution()
    
    # Test case 1: Regular case
    head1 = createLinkedList([1, 2, 3, 4, 5])
    reversed1 = solution.reverseList(head1)
    assert linkedListToArray(reversed1) == [5, 4, 3, 2, 1]
    print("Test case 1 passed!")
    
    # Test case 2: Empty list
    head2 = createLinkedList([])
    reversed2 = solution.reverseList(head2)
    assert reversed2 is None
    print("Test case 2 passed!")
    
    # Test case 3: Single node
    head3 = createLinkedList([1])
    reversed3 = solution.reverseList(head3)
    assert linkedListToArray(reversed3) == [1]
    print("Test case 3 passed!")
    
    # Test case 4: Two nodes
    head4 = createLinkedList([1, 2])
    reversed4 = solution.reverseList(head4)
    assert linkedListToArray(reversed4) == [2, 1]
    print("Test case 4 passed!")

if __name__ == "__main__":
    test_reverseList()
    print("All test cases passed!")