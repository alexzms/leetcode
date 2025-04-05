"""
Problem: 3Sum
https://leetcode.cn/problems/3sum/
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
The triplets that sum to zero are:
- [-1,0,1]
- [-1,-1,2]
Note that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

Solution Approach (Double Cursor Method):
- Time Complexity: O(n²) where n is the length of nums
- Space Complexity: O(1) excluding the space required for output
- Steps:
  1. Sort the array to handle duplicates and use two-pointer technique
  2. For each number:
     * Skip duplicates to avoid redundant triplets
     * Use two pointers (left and right) to find pairs that sum to -nums[i]
     * Skip duplicates in both pointers to avoid redundant triplets
  3. Return all valid triplets
- Key Insight: After sorting, we can use two pointers to find pairs that sum to a target value
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort array to handle duplicates and use two-pointer technique
        nums.sort()
        result = []
        
        for index in range(len(nums)):
            # Skip positive numbers as they can't be part of a zero sum
            if nums[index] > 0: 
                continue
            # Skip duplicates to avoid redundant triplets
            if index > 0 and nums[index-1] == nums[index]:
                continue
                
            value = nums[index]
            left_cur = index + 1
            right_cur = len(nums) - 1
            
            while left_cur < right_cur:
                calc_val = nums[left_cur] + nums[right_cur]
                if calc_val == -value:
                    # Found a valid triplet
                    result.append([nums[index], nums[left_cur], nums[right_cur]])
                    val_l, val_r = nums[left_cur], nums[right_cur]
                    
                    # Skip duplicates in both pointers
                    while nums[left_cur] == val_l and left_cur < right_cur:
                        left_cur += 1    
                    while nums[right_cur] == val_r and left_cur < right_cur:
                        right_cur -= 1
                elif calc_val > -value:
                    right_cur -= 1
                else:
                    left_cur += 1
            
        return result

def test_three_sum():
    solution = Solution()
    
    # Test case 1: Basic case with multiple solutions
    nums1 = [-1,0,1,2,-1,-4]
    result1 = solution.threeSum(nums1)
    assert len(result1) == 2
    assert sorted([-1,-1,2]) in [sorted(triplet) for triplet in result1]
    assert sorted([-1,0,1]) in [sorted(triplet) for triplet in result1]
    
    # Test case 2: Empty array
    assert solution.threeSum([]) == []
    
    # Test case 3: Single element
    assert solution.threeSum([0]) == []
    
    # Test case 4: No solution
    assert solution.threeSum([1,2,3,4,5]) == []
    
    # Test case 5: All zeros
    assert solution.threeSum([0,0,0]) == [[0,0,0]]
    
    # Test case 6: Duplicate numbers
    assert solution.threeSum([-2,0,0,2,2]) == [[-2,0,2]]
    
    # Test case 7: Large numbers
    nums7 = [-1000,0,1000]
    assert solution.threeSum(nums7) == [[-1000,0,1000]]
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_three_sum()
