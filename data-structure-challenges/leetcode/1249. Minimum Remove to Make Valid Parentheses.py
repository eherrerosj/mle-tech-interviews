"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions )
    so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"

Constraints:
    1 <= s.length <= 10^5
    s[i] is one of  '(' , ')' and lowercase English letters.

Learnings:
- In my initial solution I used 2 independent for loops to keep complexity at O(n). I uses a
    2 counters: one to sweep L->R and one R->L (+1 when a "(" is found, -1 when a ")" is found
    in the former, opposed signs in the later. It worked as well but code was too long because I
    didn't add the logic to an independent function and I ended up repeating code
- Instead, another good solution is to use stacks. I implemented this one to learn. The idea is to
    add the index of a "(" and pop it when a ")" is found. If there's nothing to pop and a ")" is
    found then that index must be added to the list of indexes "to be removed". We can't forget about
    all the elements remaining in the stack once the loop has finished, since those need to be added
    to the list of indexes "to be removed" as well.
- Finally, we iterate through the whole string again and only add chars whose index is not in the
    "to be removed" list
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        idx_to_remove = set()
        sol = []

        # iterate through original string and use a support stack to know when () are not balanced
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif c == ")":
                if not stack:
                    idx_to_remove.add(i)
                else:
                    stack.pop()

        # add remaining unbalanced
        idx_to_remove = idx_to_remove.union(set(stack))

        # iterate through original string and add chars only if they are not yet to be removed
        for i, c in enumerate(s):
            if i not in idx_to_remove:
                sol.append(c)
        return "".join(sol)


sol = Solution().minRemoveToMakeValid(s="hola()que tal(")
print(sol == "hola()que tal")
sol = Solution().minRemoveToMakeValid(s="a(b(c)d))")
print(sol == "a(b(c)d)")
sol = Solution().minRemoveToMakeValid(s="(a(b(c)d)")
print(sol == "a(b(c)d)")
sol = Solution().minRemoveToMakeValid(s="(")
print(sol == "")
sol = Solution().minRemoveToMakeValid(s="()")
print(sol == "()")
sol = Solution().minRemoveToMakeValid(s="")
print(sol == "")
sol = Solution().minRemoveToMakeValid(s="(()")
print(sol == "()")
