"""
Given the root node of a binary search tree and two integers low and high,
return the sum of values of all nodes with a value in the inclusive range [low, high].

Example 1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

Constraints:
    The number of nodes in the tree is in the range [1, 2 * 104].
    1 <= Node.val <= 105
    1 <= low <= high <= 105
    All Node.val are unique.

Learnings:
- I solved it with an iterative approach, although the recursive approach is also accepted
- Good thing of the iterative approach is that the stack is, at max, of depth 2, while the recursive
    approach could reach a limit
"""

from typing import List
from common.tree import TreeNode


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stack = [root]
        sol = 0
        while stack:
            node = stack.pop()
            if node:
                if node.val >= low and node.val <= high:
                    sol += node.val
                    stack.append(node.left)
                    stack.append(node.right)
                elif node.val > high:
                    stack.append(node.left)
                elif node.val < low:
                    stack.append(node.right)
        return sol


tree = TreeNode()._deserialize("[10,5,15,3,7,null,18]")

sol = Solution().rangeSumBST(root=tree, low=7, high=15)
print(sol == 32)
