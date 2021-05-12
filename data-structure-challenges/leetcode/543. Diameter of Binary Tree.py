"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
    This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    -100 <= Node.val <= 100

Learning:
- Solution must be between 2 leaf nodes
- Recursion. O(n)
"""

from typing import List


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    diameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self._longest_path(root)
        return self.diameter

    def _longest_path(self, node):
        if not node:
            return 0
        left_path = self._longest_path(node.left)
        right_path = self._longest_path(node.right)
        self.diameter = max(self.diameter, left_path + right_path)
        return max(left_path, right_path) + 1


tree = TreeNode(val=1)
tree.left = TreeNode(val=2)
tree.right = TreeNode(val=3)
tree.left.left = TreeNode(val=4)
tree.left.right = TreeNode(val=5)

sol = Solution().diameterOfBinaryTree(root=tree)
print(sol == 3)

tree = TreeNode(val=1)
tree.left = TreeNode(val=2)

sol = Solution().diameterOfBinaryTree(root=tree)
print(sol == 1)
