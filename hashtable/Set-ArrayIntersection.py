"""
Problem: Intersection of Two Arrays
https://leetcode.cn/problems/intersection-of-two-arrays/
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Solution Approaches:

1. Set Method (SolutionSet):
   - Time Complexity: O(n + m) where n and m are lengths of the arrays
   - Space Complexity: O(n + m)
   - Steps:
     1. Convert first array to a set
     2. Check each element in second array against the set
     3. Add matches to result set
     4. Convert result set to list
   - Advantages:
     * Simple and clean implementation
     * Automatically handles duplicates
     * Built-in set operations

2. HashMap Method (SolutionHashMap):
   - Time Complexity: O(n + m) where n and m are lengths of the arrays
   - Space Complexity: O(n)
   - Steps:
     1. Create a map of first array elements
     2. Mark elements that appear in second array
     3. Collect marked elements into result
   - Advantages:
     * More control over the process
     * Can be extended to count frequencies
     * Memory efficient if one array is much smaller
"""

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sol = SolutionSet()
        return sol.intersection(nums1, nums2)


class SolutionSet:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = set()
        for num in nums1:
            count.add(num)
        result = set()
        for num in nums2:
            if num in count:
                result.add(num)
        return list(result)

class SolutionHashMap:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        for num in nums1:
            count[num] = 0
        for num in nums2:
            if num in count:
                count[num] = 1
        result = []
        for key, value in count.items():
            if value != 0:
                result.append(key)
        return result

def test_intersection():
    # Test both solutions
    solution_set = SolutionSet()
    solution_hash = SolutionHashMap()
    
    # Test case 1: Basic intersection
    nums1_1 = [1,2,2,1]
    nums2_1 = [2,2]
    expected1 = [2]
    result1_set = solution_set.intersection(nums1_1, nums2_1)
    result1_hash = solution_hash.intersection(nums1_1, nums2_1)
    assert sorted(result1_set) == sorted(expected1)
    assert sorted(result1_hash) == sorted(expected1)
    
    # Test case 2: Multiple intersections
    nums1_2 = [4,9,5]
    nums2_2 = [9,4,9,8,4]
    expected2 = [9,4]
    result2_set = solution_set.intersection(nums1_2, nums2_2)
    result2_hash = solution_hash.intersection(nums1_2, nums2_2)
    assert sorted(result2_set) == sorted(expected2)
    assert sorted(result2_hash) == sorted(expected2)
    
    # Test case 3: No intersection
    nums1_3 = [1,2,3]
    nums2_3 = [4,5,6]
    expected3 = []
    result3_set = solution_set.intersection(nums1_3, nums2_3)
    result3_hash = solution_hash.intersection(nums1_3, nums2_3)
    assert result3_set == expected3
    assert result3_hash == expected3
    
    # Test case 4: Empty arrays
    nums1_4 = []
    nums2_4 = []
    expected4 = []
    result4_set = solution_set.intersection(nums1_4, nums2_4)
    result4_hash = solution_hash.intersection(nums1_4, nums2_4)
    assert result4_set == expected4
    assert result4_hash == expected4
    
    # Test case 5: One empty array
    nums1_5 = [1,2,3]
    nums2_5 = []
    expected5 = []
    result5_set = solution_set.intersection(nums1_5, nums2_5)
    result5_hash = solution_hash.intersection(nums1_5, nums2_5)
    assert result5_set == expected5
    assert result5_hash == expected5
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_intersection()
