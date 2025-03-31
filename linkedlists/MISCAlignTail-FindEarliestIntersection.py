"""
Problem: Intersection of Two Linked Lists
https://leetcode.cn/problems/intersection-of-two-linked-lists/
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'

Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection

Solution Approaches:

1. Length Difference Method (Solution):
   - Time Complexity: O(n + m) where n and m are lengths of the lists
   - Space Complexity: O(1)
   - Steps:
     1. Calculate lengths of both lists
     2. Check if tails match (early exit if no intersection)
     3. Align pointers by moving longer list's pointer
     4. Move both pointers until they meet

2. Insightful(both travel same distance) Method (SolutionElegant):
   - Time Complexity: O(n + m) where n and m are lengths of the lists
   - Space Complexity: O(1)
   - Steps:
     1. Use two pointers starting at heads of both lists
     2. When one pointer reaches end, switch to other list's head
     3. Continue until pointers meet or both reach None
   - Key Insight: Both pointers will travel same distance (n + m) before meeting
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None: return None
        listlen1 = 0
        listlen2 = 0
        curA = headA
        while curA.next is not None:
            listlen1 += 1
            curA = curA.next
        curB = headB
        while curB.next is not None:
            listlen2 += 1
            curB = curB.next
        # This judgement is not necessary, but can early-stop impolssible cases, s.t. save computation
        if curA.val != curB.val: return None
        # now they must intersect. First goto the point where they left same length
        curA, curB = headA, headB
        diff = listlen1 - listlen2
        if diff > 0:
            for _ in range(diff):
                curA = curA.next
        elif diff < 0:
            for _ in range(-diff):
                curB = curB.next
        # now they are on the point where they left same length
        # before this point, no intersection point is possible
        # after this point, just forward-loop until 'next' match
        while curA is not None:
            if curA == curB:
                return curA
            curA, curB = curA.next, curB.next
        return None

class SolutionElegant:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 处理边缘情况
        if not headA or not headB:
            return None
        
        # 在每个链表的头部初始化两个指针
        pointerA = headA
        pointerB = headB
        
        # 遍历两个链表直到指针相交
        while pointerA != pointerB:
            # 将指针向前移动一个节点
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA
        
        # 如果相交，指针将位于交点节点，如果没有交点，值为None
        return pointerA

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

def create_intersecting_lists(listA, listB, intersectVal, skipA, skipB):
    # Create list A
    headA = create_linked_list(listA)
    
    # Create list B
    headB = create_linked_list(listB)
    
    # Find intersection node
    currentA = headA
    for _ in range(skipA):
        currentA = currentA.next
    
    currentB = headB
    for _ in range(skipB):
        currentB = currentB.next
    
    # Connect lists at intersection point
    currentB.next = currentA
    
    return headA, headB

def test_get_intersection_node():
    solution1 = Solution()
    solution2 = SolutionElegant()
    
    # Test case 1: Intersecting lists
    listA = [4,1,8,4,5]
    listB = [5,6,1,8,4,5]
    headA1, headB1 = create_intersecting_lists(listA, listB, 8, 2, 3)
    result1_1 = solution1.getIntersectionNode(headA1, headB1)
    result1_2 = solution2.getIntersectionNode(headA1, headB1)
    assert result1_1.val == 8 and result1_2.val == 8
    
    # Test case 2: Another intersecting case
    listA = [1,9,1,2,4]
    listB = [3,2,4]
    headA2, headB2 = create_intersecting_lists(listA, listB, 2, 3, 1)
    result2_1 = solution1.getIntersectionNode(headA2, headB2)
    result2_2 = solution2.getIntersectionNode(headA2, headB2)
    assert result2_1.val == 2 and result2_2.val == 2
    
    # Test case 3: Non-intersecting lists
    listA = [2,6,4]
    listB = [1,5]
    headA3 = create_linked_list(listA)
    headB3 = create_linked_list(listB)
    result3_1 = solution1.getIntersectionNode(headA3, headB3)
    result3_2 = solution2.getIntersectionNode(headA3, headB3)
    assert result3_1 is None and result3_2 is None
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_get_intersection_node()