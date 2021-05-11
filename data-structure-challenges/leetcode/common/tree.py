# Definition for a binary tree node.
class TreeNode:
    seq = []

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self._left = left
        self._right = right
        self.height = 0
        self._depth = 0

    def __repr__(self):
        self._serialize_breadth_first(self)
        return self.seq.__repr__()

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value
        self.height = 0
        self._compute_tree_height(self)

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value
        self.height = 0
        self._compute_tree_height(self)

    def _serialize_pre_order(self, root):
        "Top -> Bottom, Left -> Right"
        self.seq.append(root.val)
        if root.left:
            self._serialize_pre_order(root.left)
        if root.right:
            self._serialize_pre_order(root.right)

    def _serialize_post_order(self, root):
        "Bottom -> Top, Left -> Right"
        if root.left:
            self._serialize_post_order(root.left)
        if root.right:
            self._serialize_post_order(root.right)
        self.seq.append(root.val)

    def _serialize_in_order(self, root):
        "Left -> Node -> Right"
        if root.left:
            self._serialize_in_order(root.left)
        self.seq.append(root.val)
        if root.right:
            self._serialize_in_order(root.right)

    def _serialize_breadth_first(self, root):
        "Left -> Right, Top -> Bottom"
        # TO-DO
        pass

    def _deserialize(self, string):
        if string == "{}":
            return None
        nodes = [None if val == "null" else TreeNode(int(val)) for val in string.strip("[]{}").split(",")]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        self._compute_tree_height(self)
        return root

    def _compute_tree_height(self, root):
        self._depth += 1
        self.height = max(self.height, self._depth)

        if root.left:
            self._compute_tree_height(root.left)
        elif root.right:
            self._compute_tree_height(root.right)

        self._depth -= 1
