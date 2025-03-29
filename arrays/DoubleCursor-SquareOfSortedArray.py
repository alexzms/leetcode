from typing import List

"""
Problem 977: Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100]. After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
- 1 <= nums.length <= 104
- -104 <= nums[i] <= 104
- nums is sorted in non-decreasing order.

Solution Approaches:
1. Split array into negative and non-negative parts, then merge using two pointers
2. Two pointers from both ends of the array

Time Complexity: O(n)
Space Complexity: O(n)
"""

MAX_NUM = 10001
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Split the array into two parts, one being negative, one being non-negative
        negative = []
        non_negative = []
        reverted_flag = False
        # O(n)
        for num in nums:
            if not reverted_flag and num >= 0:
                reverted_flag = True
            if not reverted_flag:
                negative.append(num)
            else:
                non_negative.append(num)
        # Two-pointer solution
        # Since the array has none-descending property, we can exploit this using pointer, getting extra information
        index_neg = len(negative) - 1 # start from the end of the negative array
        end_neg = -1 # negative array is ended when index_neg hit -1
        index_pos = 0
        end_pos = len(non_negative)
        result = []
        while index_neg != end_neg or index_pos != end_pos:
            # compare abs
            abs_neg = abs(negative[index_neg]) if index_neg != end_neg else MAX_NUM
            abs_pos = abs(non_negative[index_pos]) if index_pos != end_pos else MAX_NUM
            if abs_neg < abs_pos:
                result.append(negative[index_neg] **2)
                index_neg -= 1
            else:
                result.append(non_negative[index_pos] **2)
                index_pos += 1
        return result

class OfficialSolution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, i = 0, len(nums)-1, len(nums)-1
        res = [float('inf')] * len(nums) # 需要提前定义列表，存放结果
        while l <= r:
            if nums[l] ** 2 < nums[r] ** 2: # 左右边界进行对比，找出最大值
                res[i] = nums[r] ** 2
                r -= 1 # 右指针往左移动
            else:
                res[i] = nums[l] ** 2
                l += 1 # 左指针往右移动
            i -= 1 # 存放结果的指针需要往前平移一位
        return res


# Test cases
if __name__ == "__main__":
    solution = Solution()
    nums1 = [-4, -1, 0, 3, 10]
    print(solution.sortedSquares(nums1))  # Output: [0, 1, 9, 16, 100]
    solution = OfficialSolution()
    nums2 = [-4, -1, 0, 3, 10]
    print(solution.sortedSquares(nums2))  # Output: [0, 1, 9, 16, 100]


        