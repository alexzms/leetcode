"""
Problem: Reverse Linked List II
https://leetcode.cn/problems/reverse-linked-list-ii/
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Example 3:
Input: head = [1,2,3,4,5], left = 3, right = 4
Output: [1,2,4,3,5]

Solution Approach:
1. Use a dummy head node to handle edge cases
2. Find the start and end nodes of the portion to reverse
3. Keep track of nodes before start and after end
4. Reverse the portion between start and end using a new dummy head
5. Connect the reversed portion back to the original list
6. Return dummy_head.next as the new head
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right == 0: return head
        dummy_head = ListNode(0, head)
        before_start = dummy_head
        start = head
        end = head
        for i in range(0, right-1):
            if i < left-1:
                start = start.next
                before_start = before_start.next
            end = end.next
        after_end = end.next
        end.next = None

        dummy_head_reverse = ListNode(0, None)
        cur = start
        while cur is not None:
            next_node = cur.next
            cur.next = dummy_head_reverse.next
            dummy_head_reverse.next = cur
            cur = next_node
        before_start.next = dummy_head_reverse.next
        start.next = after_end

        return dummy_head.next


# Solution identical to the above, but it explicitly uses a single sweep
class SolutionExplicitSingleSweep:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right == 0: return head
        dummy_head = ListNode(0, head)
        dummy_head_reverse = ListNode(0, None)
        before_start = dummy_head
        start = head
        end = head

        counter = 0
        while True:
            counter += 1
            if counter == left:
                # start reversing
                for _ in range(right-left+1):
                    next_node = start.next
                    start.next = dummy_head_reverse.next
                    dummy_head_reverse.next = start
                    start = next_node
                before_start.next = dummy_head_reverse.next
                end.next = start
                break
            else:
                before_start = before_start.next
                start = start.next
                end = end.next

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

def test_reverse_between():
    solution = Solution()
    
    # Test case 1: [1,2,3,4,5], left=2, right=4 -> [1,4,3,2,5]
    head1 = create_linked_list([1,2,3,4,5])
    result1 = solution.reverseBetween(head1, 2, 4)
    assert linked_list_to_array(result1) == [1,4,3,2,5]
    
    # Test case 2: [5], left=1, right=1 -> [5]
    head2 = create_linked_list([5])
    result2 = solution.reverseBetween(head2, 1, 1)
    assert linked_list_to_array(result2) == [5]
    
    # Test case 3: [1,2,3,4,5], left=3, right=4 -> [1,2,4,3,5]
    head3 = create_linked_list([1,2,3,4,5])
    result3 = solution.reverseBetween(head3, 3, 4)
    assert linked_list_to_array(result3) == [1,2,4,3,5]
    
    # Test case 4: [1,2,3,4,5], left=1, right=5 -> [5,4,3,2,1]
    head4 = create_linked_list([1,2,3,4,5])
    result4 = solution.reverseBetween(head4, 1, 5)
    assert linked_list_to_array(result4) == [5,4,3,2,1]
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_reverse_between()



        

