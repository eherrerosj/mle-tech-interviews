"""
Given two non-negative integers, num1 and num2 represented as string,
    return the sum of num1 and num2 as a string.


Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"

Constraints:
    1 <= num1.length, num2.length <= 104
    num1 and num2 consist of only digits.
    num1 and num2 don't have any leading zeros except for the zero itself.

Learnings:
- Usage of ord("num") - ord("0")
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = list(num1), list(num2)
        carry, res = 0, []
        while len(num2) > 0 or len(num1) > 0:
            n1 = ord(num1.pop()) - ord("0") if len(num1) > 0 else 0
            n2 = ord(num2.pop()) - ord("0") if len(num2) > 0 else 0

            temp = n1 + n2 + carry
            res.append(temp % 10)
            carry = temp // 10
        if carry:
            res.append(carry)
        return "".join([str(i) for i in res])[::-1]


sol = Solution().addStrings(num1="456", num2="77")
print(sol == "533")
