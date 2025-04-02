"""
Problem: Linked List Cycle
https://leetcode.cn/problems/linked-list-cycle/
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Solution Approach (Floyd's Cycle Detection Algorithm):
- Time Complexity: O(n) where n is the number of nodes
- Space Complexity: O(1)
- Steps:
  1. Use two pointers: fast (moves 2 steps) and slow (moves 1 step)
  2. If there's a cycle, fast and slow pointers will eventually meet
  3. If there's no cycle, fast pointer will reach None
- Key Insight: If there's a cycle, fast pointer will catch up to slow pointer
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None: return False
        fast_cur = head
        slow_cur = head
        while True:
            fast_cur = fast_cur.next
            if fast_cur is None:
                return False
            fast_cur = fast_cur.next
            if fast_cur is None:
                return False
            slow_cur = slow_cur.next
            if slow_cur == fast_cur:
                return True

# Test cases
def create_linked_list(arr, pos):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    cycle_node = None
    
    # Create the linked list
    for i, val in enumerate(arr[1:], 1):
        current.next = ListNode(val)
        current = current.next
        if i == pos:
            cycle_node = current
    
    # Create cycle if pos is valid
    if pos > 0:
        current.next = cycle_node
    if pos == 0:
        current.next = head
    
    return head

def test_has_cycle():
    solution = Solution()
    
    # Test case 1: [3,2,0,-4], pos = 1
    head1 = create_linked_list([3,2,0,-4], 1)
    assert solution.hasCycle(head1) == True
    
    # Test case 2: [1,2], pos = 0
    head2 = create_linked_list([1,2], 0)
    assert solution.hasCycle(head2) == True
    
    # Test case 3: [1], pos = -1
    head3 = create_linked_list([1], -1)
    assert solution.hasCycle(head3) == False
    
    # Test case 4: [], pos = -1
    head4 = create_linked_list([], -1)
    assert solution.hasCycle(head4) == False
    
    # Test case 5: [1,2,3,4,5], pos = 2
    head5 = create_linked_list([1,2,3,4,5], 2)
    assert solution.hasCycle(head5) == True
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_has_cycle()
            