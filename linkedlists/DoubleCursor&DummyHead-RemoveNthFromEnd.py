"""
Problem: Remove Nth Node From End of List
https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Solution Approach:
1. Use a dummy head node to handle edge cases
2. Use two pointers (pointer1 and pointer2) with a gap of n nodes
3. Move pointer1 ahead until it reaches the end
4. When pointer1 reaches the end, pointer2 will be at the nth node from the end
5. Remove the node at pointer2 by updating the connection
6. Return dummy_head.next as the new head
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        pointer1 = head
        before_ptr2 = dummy_head
        pointer2 = head
        ahead = 0
        while True:
            pointer1 = pointer1.next
            if pointer1 is None:
                break
            ahead += 1
            if ahead == n:
                before_ptr2 = pointer2
                pointer2 = pointer2.next
                ahead -= 1
        # remove pointer2
        before_ptr2.next = pointer2.next
        return dummy_head.next

# Test cases
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_remove_nth_from_end():
    solution = Solution()
    
    # Test case 1: [1,2,3,4,5], n=2 -> [1,2,3,5]
    head1 = create_linked_list([1,2,3,4,5])
    result1 = solution.removeNthFromEnd(head1, 2)
    assert linked_list_to_array(result1) == [1,2,3,5]
    
    # Test case 2: [1], n=1 -> []
    head2 = create_linked_list([1])
    result2 = solution.removeNthFromEnd(head2, 1)
    assert result2 is None
    
    # Test case 3: [1,2], n=1 -> [1]
    head3 = create_linked_list([1,2])
    result3 = solution.removeNthFromEnd(head3, 1)
    assert linked_list_to_array(result3) == [1]
    
    # Test case 4: [1,2,3], n=3 -> [2,3]
    head4 = create_linked_list([1,2,3])
    result4 = solution.removeNthFromEnd(head4, 3)
    assert linked_list_to_array(result4) == [2,3]
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_remove_nth_from_end()
        
