"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701

Constraints:
    1 <= s.length <= 7
    s consists only of uppercase English letters.
    s is between "A" and "FXSHRXW".
"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        print(f"\nString: {s}")
        start = 65  # A
        end = 90  # Z
        alphabet = {chr(i): i - 64 for i in range(start, end + 1)}
        return sum([26 ** (i) * alphabet[a] for i, a in enumerate(s[::-1])])


sol = Solution()
print(sol.titleToNumber("A"))
print(sol.titleToNumber("B"))
print(sol.titleToNumber("AB"))
print(sol.titleToNumber("ZY"))
