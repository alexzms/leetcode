"""
Problem: Missing Number
https://leetcode.cn/problems/missing-number/
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
2 is the missing number since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 
2 is the missing number since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
8 is the missing number since it does not appear in nums.

Solution Approach (XOR Method):
- Time Complexity: O(n)
- Space Complexity: O(1)
- Key Insight: Use XOR properties
  1. a ^ a = 0 (number XOR itself equals 0)
  2. a ^ 0 = a (number XOR 0 equals itself)
  3. XOR is associative and commutative
- Steps:
  1. XOR all numbers in array
  2. XOR all numbers from 1 to n
  3. Result is the missing number because:
     - All numbers except the missing one appear twice (once in array, once in range)
     - Numbers appearing twice cancel out (become 0)
     - Only the missing number remains
"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_buff = 0
        # XOR all numbers in array
        for num in nums:
            xor_buff ^= num
        # XOR all numbers from 1 to n
        for i in range(1, len(nums) + 1):
            xor_buff ^= i
        return xor_buff

def test_missing_number():
    solution = Solution()
    
    # Test case 1: [3,0,1]
    nums1 = [3,0,1]
    assert solution.missingNumber(nums1) == 2
    
    # Test case 2: [0,1]
    nums2 = [0,1]
    assert solution.missingNumber(nums2) == 2
    
    # Test case 3: [9,6,4,2,3,5,7,0,1]
    nums3 = [9,6,4,2,3,5,7,0,1]
    assert solution.missingNumber(nums3) == 8
    
    # Test case 4: [0]
    nums4 = [0]
    assert solution.missingNumber(nums4) == 1
    
    # Test case 5: [1]
    nums5 = [1]
    assert solution.missingNumber(nums5) == 0
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_missing_number()
