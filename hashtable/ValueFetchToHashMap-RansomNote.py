"""
Problem: Ransom Note
https://leetcode.cn/problems/ransom-note/
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Solution Approach (Hash Map Method):
- Time Complexity: O(m) where m is the length of magazine
- Space Complexity: O(1) since we store at most 26 characters (lowercase letters)
- Steps:
  1. Create a hash map to count occurrences of each character in magazine
  2. For each character in ransomNote:
     * If character not in map or count is 0, return false
     * Otherwise, decrement the count
  3. Return true if all characters were found
- Key Insight: We only need to track the frequency of each character. Optimize the fetch complexity by using hashmap.
"""

from typing import List

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create a hash map to count characters in magazine
        alphabet = {}
        for c in magazine:
            if c not in alphabet:
                alphabet[c] = 1
            else:
                alphabet[c] += 1
        
        # Check if we can construct ransomNote
        for c in ransomNote:
            if c not in alphabet:
                return False
            elif alphabet[c] == 0:
                return False
            else:
                alphabet[c] -= 1
        return True

def test_can_construct():
    solution = Solution()
    
    # Test case 1: Basic false case
    assert solution.canConstruct("a", "b") == False
    
    # Test case 2: Not enough characters
    assert solution.canConstruct("aa", "ab") == False
    
    # Test case 3: Valid case
    assert solution.canConstruct("aa", "aab") == True
    
    # Test case 4: Empty strings
    assert solution.canConstruct("", "") == True
    assert solution.canConstruct("", "a") == True
    assert solution.canConstruct("a", "") == False
    
    # Test case 5: Case sensitivity
    assert solution.canConstruct("Aa", "aa") == False
    
    # Test case 6: Multiple occurrences
    assert solution.canConstruct("aaa", "aaaa") == True
    assert solution.canConstruct("aaaa", "aaa") == False
    
    # Test case 7: Different characters
    assert solution.canConstruct("abc", "def") == False
    assert solution.canConstruct("abc", "abcdef") == True
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_can_construct()