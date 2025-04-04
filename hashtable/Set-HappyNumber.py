"""
Problem: Happy Number
https://leetcode.cn/problems/happy-number/
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
1. Starting with any positive integer, replace the number by the sum of the squares of its digits.
2. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
3. Those numbers for which this process ends in 1 are happy.

Example 1:
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:
Input: n = 2
Output: false
Explanation:
2^2 = 4
4^2 = 16
1^2 + 6^2 = 37
3^2 + 7^2 = 58
5^2 + 8^2 = 89
8^2 + 9^2 = 145
1^2 + 4^2 + 5^2 = 42
4^2 + 2^2 = 20
2^2 + 0^2 = 4 (cycle detected)

Solution Approach (Set Method):
- Time Complexity: O(log n) for each step, O(log n) steps
- Space Complexity: O(log n) to store seen numbers
- Steps:
  1. Use a set to track seen numbers
  2. Calculate sum of squares of digits
  3. If sum is 1, return true
  4. If sum is in set, return false (cycle detected)
  5. Otherwise, add sum to set and continue
- Key Insight: Numbers either reach 1 or enter a cycle
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        # Use a set to track seen numbers and detect cycles
        history = set()
        number = n
        
        while True:
            # Calculate sum of squares of digits
            calc_result = 0
            while number >= 10:
                residual = number % 10
                calc_result += residual ** 2
                number //= 10
            calc_result += number**2
            
            # Check if we've found a happy number or a cycle
            if calc_result in history:
                return False
            if calc_result == 1:
                return True
            else:
                history.add(calc_result)
            number = calc_result

def test_is_happy():
    solution = Solution()
    
    # Test case 1: Happy number
    assert solution.isHappy(19) == True
    
    # Test case 2: Not a happy number
    assert solution.isHappy(2) == False
    
    # Test case 3: Single digit happy number
    assert solution.isHappy(1) == True
    
    # Test case 4: Another happy number
    assert solution.isHappy(7) == True
    
    # Test case 5: Another non-happy number
    assert solution.isHappy(4) == False
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_is_happy()
