"""
Problem: Valid Anagram
https://leetcode.cn/problems/valid-anagram/
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Solution Approach (Hashtable Method):
- Time Complexity: O(n) where n is the length of the strings
- Space Complexity: O(k) where k is the size of the character set
- Steps:
  1. Count the frequency of each character in string s
  2. Iterate through string t and decrement counts
  3. If any character in t is not in the map or count < 0, return false
  4. Check if all counts are 0 at the end
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create a hashtable to store character frequencies
        char_dict = {} # This is a hashtable in python
        
        # Count frequencies of characters in string s
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
                
        # Decrement frequencies based on string t
        for char in t:
            if char in char_dict:
                char_dict[char] -= 1
                if char_dict[char] < 0:
                    return False
            else:
                return False
                
        # Ensure all characters were used exactly the same number of times
        for _, value in char_dict.items():
            if value != 0:
                return False
        return True

def test_is_anagram():
    solution = Solution()
    
    # Test case 1: Valid anagram
    s1, t1 = "anagram", "nagaram"
    assert solution.isAnagram(s1, t1) == True
    
    # Test case 2: Invalid anagram
    s2, t2 = "rat", "car"
    assert solution.isAnagram(s2, t2) == False
    
    # Test case 3: Different lengths
    s3, t3 = "ab", "a"
    assert solution.isAnagram(s3, t3) == False
    
    # Test case 4: Empty strings
    s4, t4 = "", ""
    assert solution.isAnagram(s4, t4) == True
    
    # Test case 5: Same characters, different frequencies
    s5, t5 = "aacc", "aabc"
    assert solution.isAnagram(s5, t5) == False
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_is_anagram()
