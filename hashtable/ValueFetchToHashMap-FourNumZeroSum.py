"""
Problem: 4Sum II
https://leetcode.cn/problems/4sum-ii/
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:
0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Example 1:
Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

Example 2:
Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1

Solution Approach (Hash Map Method):
- Time Complexity: O(n²) where n is the length of each array
- Space Complexity: O(n²) to store the hash map of sums
- Steps:
  1. Create a hash map to store sums of pairs from nums1 and nums2
  2. For each pair in nums3 and nums4:
     * Check if the negative of their sum exists in the hash map
     * If it exists, add the count of occurrences to the result
  3. Return the total count
- Key Insight: Instead of checking all quadruplets (O(n⁴)), we can split the problem into two pairs
"""

from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # Create a hash map to store sums of pairs from nums1 and nums2
        sum12 = {}
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 not in sum12:
                    sum12[n1+n2] = 1
                else:
                    sum12[n1+n2] += 1
        
        # Count quadruplets that sum to zero
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                if -(n3+n4) in sum12.keys():
                    count += sum12[-(n3+n4)]
        return count

def test_four_sum_count():
    solution = Solution()
    
    # Test case 1: Basic case
    nums1 = [1,2]
    nums2 = [-2,-1]
    nums3 = [-1,2]
    nums4 = [0,2]
    assert solution.fourSumCount(nums1, nums2, nums3, nums4) == 2
    
    # Test case 2: Single element arrays
    nums1 = [0]
    nums2 = [0]
    nums3 = [0]
    nums4 = [0]
    assert solution.fourSumCount(nums1, nums2, nums3, nums4) == 1
    
    # Test case 3: No valid quadruplets
    nums1 = [1]
    nums2 = [1]
    nums3 = [1]
    nums4 = [1]
    assert solution.fourSumCount(nums1, nums2, nums3, nums4) == 0
    
    # Test case 4: Multiple valid combinations
    nums1 = [-1,-1]
    nums2 = [-1,1]
    nums3 = [-1,1]
    nums4 = [1,-1]
    assert solution.fourSumCount(nums1, nums2, nums3, nums4) == 6
    
    # Test case 5: Larger arrays
    nums1 = [0,1,-1]
    nums2 = [-1,1,0]
    nums3 = [0,0,1]
    nums4 = [-1,1,1]
    result = solution.fourSumCount(nums1, nums2, nums3, nums4)
    assert result > 0  # Should have at least one valid quadruplet
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_four_sum_count()
        