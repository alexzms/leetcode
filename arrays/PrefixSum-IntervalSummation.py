"""
Problem:
Given an array of integers and multiple interval queries [a,b], find the sum of elements from index a to index b (inclusive).

Solution:
Use prefix sum technique to precompute cumulative sums, then calculate interval sum in O(1) time by subtracting prefix sums:
sum(a,b) = prefix_sum[b] - prefix_sum[a-1] (or just prefix_sum[b] if a=0)
"""

class Solution:
    def intervalSum(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Build prefix sum array
        prefix_sum = []
        for i in range(len(nums)):
            if i == 0:
                prefix_sum.append(nums[i])
            else:
                prefix_sum.append(prefix_sum[i-1] + nums[i])
        
        # Process queries
        results = []
        for a, b in queries:
            minus = prefix_sum[a-1] if a != 0 else 0
            results.append(prefix_sum[b] - minus)
        
        return results

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3, 4, 5]
    queries1 = [[0, 2], [1, 3], [2, 4]]
    expected1 = [6, 9, 12]
    
    # Test case 2
    nums2 = [-5, 10, -3, 8, 2]
    queries2 = [[0, 4], [1, 3], [2, 2]]
    expected2 = [12, 15, -3]
    
    sol = Solution()
    
    # Run test cases
    results1 = sol.intervalSum(nums1, queries1)
    results2 = sol.intervalSum(nums2, queries2)
    
    print("Test Case 1:")
    print(f"Input: nums = {nums1}, queries = {queries1}")
    print(f"Expected: {expected1}")
    print(f"Output: {results1}")
    print(f"Passed: {results1 == expected1}")
    
    print("\nTest Case 2:")
    print(f"Input: nums = {nums2}, queries = {queries2}")
    print(f"Expected: {expected2}")
    print(f"Output: {results2}")
    print(f"Passed: {results2 == expected2}")
    
    # You can also handle input as in the original implementation
    """
    # Original input handling
    arr = []
    length = int(input())
    nums = []
    for i in range(length):
        nums.append(int(input()))
    
    queries = []
    while True:
        try:
            str_in = input()
            a, b = str_in.split(' ')
            a, b = int(a), int(b)
            queries.append([a, b])
        except:
            break
    
    sol = Solution()
    results = sol.intervalSum(nums, queries)
    for result in results:
        print(result)
    """