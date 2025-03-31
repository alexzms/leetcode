"""
Problem: Reverse a singly linked list
https://leetcode.cn/problems/reverse-linked-list/
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Solution Approach(Iteration):
Using two pointers (pre_node and cur_node) to reverse the list:
1. Keep track of previous node (pre_node)
2. For each current node:
   - Store next node
   - Reverse the link (point current node to previous)
   - Move previous to current
   - Move current to next
3. Return the last node (which becomes the new head)

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(1) as we only use a constant amount of extra space

Solution Approach(Recursion):
1. Base case: if current node is None, return previous node
2. Recursively reverse the rest of the list
3. Reverse the current node's link
4. Return the new head (which is the last node)

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(n) due to the recursive call stack
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SolutionIteration:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        if head is None: return head
        cur_node = head
        pre_node = None
        while True:
            next_node = cur_node.next
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = next_node
            if cur_node is None:
                break
        return pre_node

class SolutionRecursive:
    def reverse(self, cur: ListNode, pre: ListNode):
        if cur is None: return pre
        next_node = cur.next
        cur.next = pre
        return self.reverse(next_node, cur)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head, None)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sol = SolutionIteration()
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