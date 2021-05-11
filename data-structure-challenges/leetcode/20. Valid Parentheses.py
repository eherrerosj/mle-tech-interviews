"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        opening_chars = "([{"
        closing_chars = ")]}"

        for c in s:
            if c in opening_chars:
                q.append(c)
            elif c in closing_chars:
                try:
                    char = q.pop()
                    if opening_chars.index(char) != closing_chars.index(c):
                        return False
                except:
                    return False
        return len(q) == 0


sol = Solution()
print(sol.isValid("(){}}{"))
