"""
Problem: Swap Nodes in Pairs
https://leetcode.cn/problems/swap-nodes-in-pairs/
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Solution Approach:
1. Use a dummy head node to handle edge cases
2. Keep track of previous_second node to maintain connections
3. For each pair:
   - Store first and second nodes
   - Update connections to swap the pair
   - Move previous_second to first node
   - Move first to next unprocessed node
4. Return dummy_head.next as the new head
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        dummy_head = ListNode(0, head)
        previous_second = dummy_head
        first = head
        second = None
        while first is not None:
            second = first.next
            if second is None:
                break
            first.next = second.next
            second.next = first
            previous_second.next = second
            previous_second = first
            first = first.next
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

def test_swap_pairs():
    solution = Solution()
    
    # Test case 1: [1,2,3,4] -> [2,1,4,3]
    head1 = create_linked_list([1,2,3,4])
    result1 = solution.swapPairs(head1)
    assert linked_list_to_array(result1) == [2,1,4,3]
    
    # Test case 2: [] -> []
    head2 = create_linked_list([])
    result2 = solution.swapPairs(head2)
    assert result2 is None
    
    # Test case 3: [1] -> [1]
    head3 = create_linked_list([1])
    result3 = solution.swapPairs(head3)
    assert linked_list_to_array(result3) == [1]
    
    # Test case 4: [1,2,3,4,5] -> [2,1,4,3,5]
    head4 = create_linked_list([1,2,3,4,5])
    result4 = solution.swapPairs(head4)
    assert linked_list_to_array(result4) == [2,1,4,3,5]
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_swap_pairs()
