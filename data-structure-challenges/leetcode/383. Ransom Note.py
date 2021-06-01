"""
Given two stings ransomNote and magazine, return true if ransomNote can be
    constructed from magazine and false otherwise.

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

Constraints:
    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.

Learnings:
- Solved it using a single hashmap, adding 1 when building it with magazine and substracting
    1 when looping through the ransomNote
- 2 missed nice optimizations:
    1. return False if note length is longer than magazine's
    2. build-up the hashmap with the Counter class from collections module
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not ransomNote:
            return True
        if not magazine or len(ransomNote) > len(magazine):
            return False

        hm = {}

        for letter in magazine:
            if letter not in hm:
                hm[letter] = 1
            else:
                hm[letter] += 1

        for letter in ransomNote:
            if letter in hm:
                if hm[letter] == 0:
                    return False
                else:
                    hm[letter] -= 1
            else:
                return False
        return True
