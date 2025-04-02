"""
Problem: Single Number
https://leetcode.cn/problems/single-number/
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Solution Approach (XOR Method):
- Time Complexity: O(n)
- Space Complexity: O(1)
- Key Insight: Use XOR properties
  1. a ^ a = 0 (number XOR itself equals 0)
  2. a ^ 0 = a (number XOR 0 equals itself)
  3. XOR is associative and commutative
- Steps:
  1. XOR all numbers in array
  2. Result is the single number because:
     - All numbers that appear twice cancel out (become 0)
     - Only the single number remains (XORed with 0)
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_buff = 0
        for num in nums:
            xor_buff ^= num
        return xor_buff

def test_single_number():
    solution = Solution()
    
    # Test case 1: [2,2,1]
    nums1 = [2,2,1]
    assert solution.singleNumber(nums1) == 1
    
    # Test case 2: [4,1,2,1,2]
    nums2 = [4,1,2,1,2]
    assert solution.singleNumber(nums2) == 4
    
    # Test case 3: [1]
    nums3 = [1]
    assert solution.singleNumber(nums3) == 1
    
    # Test case 4: [-1,-1,2]
    nums4 = [-1,-1,2]
    assert solution.singleNumber(nums4) == 2
    
    # Test case 5: [1,0,1]
    nums5 = [1,0,1]
    assert solution.singleNumber(nums5) == 0
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_single_number()