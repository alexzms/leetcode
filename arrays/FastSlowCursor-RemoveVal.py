from typing import List

"""
Problem: Remove Element https://leetcode.cn/problems/remove-element/
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
The order of elements can be changed, and you should place the resulting elements in the first part of the array.

Solution: Fast and Slow Cursor (Two-Pointer) Technique
- We use two pointers: store_index (slow) and search_index (fast)
- store_index keeps track of where to place the next valid element
- search_index scans through the array looking for elements != val
- When we find a non-target element, we copy it to the position at store_index
- This effectively removes target elements by overwriting their positions
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize slow pointer (where to store next valid element)
        store_index = 0
        original_len = len(nums)
        removed_num = 0
        
        # Fast pointer iterates through the array
        for search_index in range(len(nums)):
            if nums[search_index] != val:
                # Element is not the target value, keep it by copying to the position at store_index
                nums[store_index] = nums[search_index]
                store_index += 1
            else:
                # Element equals target value, skip it (effectively removing it)
                removed_num += 1
                
        return original_len - removed_num

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Remove value 3
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = solution.removeElement(nums1, val1)
    print(f"Test case 1: k = {k1}, nums = {nums1[:k1]}")
    
    # Test case 2: Remove value 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = solution.removeElement(nums2, val2)
    print(f"Test case 2: k = {k2}, nums = {nums2[:k2]}")
