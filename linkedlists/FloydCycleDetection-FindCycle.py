"""
Problem: Linked List Cycle II
https://leetcode.cn/problems/linked-list-cycle-ii/
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: Return the node with value 2
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: Return the node with value 1
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: null
Explanation: There is no cycle in the linked list.

Solution Approach (Floyd's Cycle Detection Algorithm with Mathematical Insight):
- Time Complexity: O(n) where n is the number of nodes
- Space Complexity: O(1)
- Steps:
  1. Use fast-slow pointers to detect cycle existence
  2. When pointers meet, use mathematical insight to find cycle start:
     - Let t be total ticks (time)
     - Let l be length before cycle
     - Let R be distance slow pointer moved before meeting
     - Let k be cycle length
     - We can prove: l = (n-1)*k + (k-R)
     - This means: if we start one pointer from head and one from meeting point,
       they will meet at cycle start
  3. Move two pointers at same speed to find cycle start
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        # first, use fast-slow cursor to determine the existence of cycle
        fast_cur = head
        slow_cur = head
        while True:
            fast_cur = fast_cur.next
            if fast_cur is None:
                return None
            fast_cur = fast_cur.next
            if fast_cur is None:
                return None
            slow_cur = slow_cur.next
            if slow_cur == fast_cur:
                break
        # The problem is modeled as t(ticks), l(len before cycle), R(slow_cur moves - l), k(cycle len)
        # We can formulate t = n*k, t - l = R, l = t - R = n*k - R. n is fast_cur cycle number
        # l = n*k - R = (n-1)*k + (k-R), n at least is 1
        # Which means, if we put cursor from head and from slow_cur, start moving with step speed = 1
        # They will meet at the cycle start point.
        # Now based on the mathematical deduction, simultaneously move cursor
        simul_pos1 = head
        simul_pos2 = slow_cur
        while simul_pos1 != simul_pos2:
            simul_pos1 = simul_pos1.next
            simul_pos2 = simul_pos2.next
        return simul_pos1

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

def test_detect_cycle():
    solution = Solution()
    
    # Test case 1: [3,2,0,-4], pos = 1
    head1 = create_linked_list([3,2,0,-4], 1)
    result1 = solution.detectCycle(head1)
    assert result1.val == 2
    
    # Test case 2: [1,2], pos = 0
    head2 = create_linked_list([1,2], 0)
    result2 = solution.detectCycle(head2)
    assert result2.val == 1
    
    # Test case 3: [1], pos = -1
    head3 = create_linked_list([1], -1)
    result3 = solution.detectCycle(head3)
    assert result3 is None
    
    # Test case 4: [], pos = -1
    head4 = create_linked_list([], -1)
    result4 = solution.detectCycle(head4)
    assert result4 is None
    
    # Test case 5: [1,2,3,4,5], pos = 2
    head5 = create_linked_list([1,2,3,4,5], 2)
    result5 = solution.detectCycle(head5)
    assert result5.val == 3
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_detect_cycle()
