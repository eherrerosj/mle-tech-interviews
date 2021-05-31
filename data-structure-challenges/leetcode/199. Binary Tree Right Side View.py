"""
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

Learnings:
- Easiest is to use recursive DFS + condition on depth
- Another interesting solution is to use BFS: One Queue + Sentinel
"""

from typing import List
from common.tree import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.sol = []
        if not root:
            return []
        self._rightSideView(root, 0)
        return self.sol

    def _rightSideView(self, root, level):
        if len(self.sol) == level:
            self.sol.append(root.val)
        if root.right:
            print(f"Appending {root.right}")
            self._rightSideView(root.right, level + 1)
        if root.left:
            print(f"Appending {root.left}")
            self._rightSideView(root.left, level + 1)
