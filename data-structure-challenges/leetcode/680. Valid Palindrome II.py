"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false

Constraints:
    1 <= s.length <= 105
    s consists of lowercase English letters.

Learning:
- Two pointer solution can't be improved
- Watch out for corner cases
- Only one letter can be removed. The whole substrings left after that can be directly checked wholy,
    without continuing the loop
"""

from typing import List


class Solution:
    def validPalindrome(self, s: str) -> bool:
        s_len = len(s)
        left = 0
        right = s_len - 1

        if s_len < 3:
            return True

        while left < right:
            if s[right] != s[left]:
                delete_l = s[left + 1 : right + 1]
                delete_r = s[left:right]
                return delete_l == delete_l[::-1] or delete_r == delete_r[::-1]
            left += 1
            right -= 1
        return True


sol = Solution().validPalindrome(s="abca")
print(sol is True)

sol = Solution().validPalindrome(s="aba")
print(sol is True)

sol = Solution().validPalindrome(s="abc")
print(sol is False)

sol = Solution().validPalindrome(s="abbbbac")
print(sol is True)

sol = Solution().validPalindrome(s="bbbba")
print(sol is True)

sol = Solution().validPalindrome(s="atbbga")
print(sol is False)

sol = Solution().validPalindrome(s="abca")
print(sol is True)


sol = Solution().validPalindrome(s="eedede")
print(sol is True)

sol = Solution().validPalindrome(s="ebcbbececabbacecbbcbe")
print(sol is True)
