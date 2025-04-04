# 首先我再强调一下 什么时候使用哈希法，当我们需要查询一个元素是否出现过，或者一个元素是否在集合里的时候，就要第一时间想到哈希法。

"""
Problem: Two Sum
https://leetcode.cn/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the two numbers in nums such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Solution Approach (Hash Map Method):
- Time Complexity: O(n) where n is the length of nums
- Space Complexity: O(n) to store the hash map
- Steps:
  1. Create a hash map to store complements (target - num) and their indices
  2. For each number:
     * If it exists in the map, we found our pair
     * Otherwise, store its complement (target - num) with its index
  3. Return the pair of indices
- Key Insight: For each number, we only need to check if its complement exists, and if we use array to store the result
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hash map to store complements and their indices
        history = {}
        
        for i in range(len(nums)):
            num = nums[i]
            # If the current number is a complement of a previous number
            if num in history.keys():
                return [i, history[num]]
            else:
                # Store the complement of the current number
                history[target - num] = i

def test_two_sum():
    solution = Solution()
    
    # Test case 1: Basic case
    nums1 = [2,7,11,15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    assert sorted(result1) == [0,1]
    
    # Test case 2: Numbers not in sequence
    nums2 = [3,2,4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    assert sorted(result2) == [1,2]
    
    # Test case 3: Duplicate numbers
    nums3 = [3,3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    assert sorted(result3) == [0,1]
    
    # Test case 4: Negative numbers
    nums4 = [-1,-2,-3,-4,-5]
    target4 = -8
    result4 = solution.twoSum(nums4, target4)
    assert sorted(result4) == [2,4]
    
    # Test case 5: Zero and positive numbers
    nums5 = [0,4,3,0]
    target5 = 0
    result5 = solution.twoSum(nums5, target5)
    assert sorted(result5) == [0,3]
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_two_sum()
