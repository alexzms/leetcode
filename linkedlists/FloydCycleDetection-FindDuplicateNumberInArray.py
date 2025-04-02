"""
Problem: Find the Duplicate Number
https://leetcode.cn/problems/find-the-duplicate-number/
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [1,1]
Output: 1

Solution Approach (Floyd's Cycle Detection on Array):
- Time Complexity: O(n) where n is the length of array
- Space Complexity: O(1)
- Key Insight: Transform array into linked list structure
  - Each index i points to nums[i]
  - This creates a linked list where duplicate number creates a cycle
  - Example: [1,3,4,2,2] creates: 0->1->3->2->4->2->4->2...
- Steps:
  1. Use fast-slow pointers to detect cycle
  2. When pointers meet, use mathematical insight to find cycle start
  3. The index at cycle start is the duplicate number
- Why it works:
  - If there's a duplicate number k, it means two different indices i,j point to k
  - This creates a cycle in our linked list structure
  - The cycle start point index is the duplicate number
"""

from typing import List

class Solution:
    # I transform this problem into detectCycleII. Check that problem
    # The link relation is defined as 0->nums[0]->nums[nums[0]]->nums[nums[nums[0]]]...
    # When there is a loop, that must means there are duplicate number
    #  because the number(as index) is pointing to the same position(means same number).
    # So our task is to find the cycle start, and the number pointing to that start, is duplication
    def findDuplicate(self, nums: List[int]) -> int:
        slow_index= 0
        fast_index= 0
        # This leetcode problem ensures testcase always have duplication, so this is finite
        while True:
            slow_index = nums[slow_index]
            fast_index = nums[nums[fast_index]]
            if slow_index == fast_index:
                break
        simul_index1 = nums[0]
        simul_index2 = nums[slow_index]
        while simul_index1 != simul_index2:
            simul_index1 = nums[simul_index1]
            simul_index2 = nums[simul_index2]
        return simul_index1

def test_find_duplicate():
    solution = Solution()
    
    # Test case 1: [1,3,4,2,2]
    nums1 = [1,3,4,2,2]
    assert solution.findDuplicate(nums1) == 2
    
    # Test case 2: [3,1,3,4,2]
    nums2 = [3,1,3,4,2]
    assert solution.findDuplicate(nums2) == 3
    
    # Test case 3: [1,1]
    nums3 = [1,1]
    assert solution.findDuplicate(nums3) == 1
    
    # Test case 4: [1,2,3,4,5,5]
    nums4 = [1,2,3,4,5,5]
    assert solution.findDuplicate(nums4) == 5
    
    # Test case 5: [2,2,2,2,2]
    nums5 = [2,2,2,2,2]
    assert solution.findDuplicate(nums5) == 2
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_find_duplicate()
        
        