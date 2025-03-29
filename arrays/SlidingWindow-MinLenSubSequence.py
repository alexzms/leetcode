from typing import List

"""
Problem 209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = 100001
        window_start = 0
        sums = 0
        for window_end in range(len(nums)):
            sums += nums[window_end]
            while sums >= target:
                current_length = window_end - window_start + 1
                print(window_start, window_end, sums)
                if current_length < min_length:
                    min_length = current_length
                if window_start < window_end:
                    sums -= nums[window_start]
                    window_start += 1
                else:
                    return 1
        return min_length if min_length != 100001 else 0


# Test cases
if __name__ == "__main__":
    sol = Solution()
    from typing import List
    
    # Test case 1
    target = 7
    nums = [2,3,1,2,4,3]
    print(f"Test 1: target = {target}, nums = {nums}")
    print(f"Expected output: 2, Actual output: {sol.minSubArrayLen(target, nums)}")
    
    # Test case 2
    target = 4
    nums = [1,4,4]
    print(f"Test 2: target = {target}, nums = {nums}")
    print(f"Expected output: 1, Actual output: {sol.minSubArrayLen(target, nums)}")
    
    # Test case 3
    target = 11
    nums = [1,1,1,1,1,1,1,1]
    print(f"Test 3: target = {target}, nums = {nums}")
    print(f"Expected output: 0, Actual output: {sol.minSubArrayLen(target, nums)}")
    
    # Test case 4
    target = 15
    nums = [1,2,3,4,5]
    print(f"Test 4: target = {target}, nums = {nums}")
    print(f"Expected output: 5, Actual output: {sol.minSubArrayLen(target, nums)}")
    
