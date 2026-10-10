# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:  # runtime O(?), space O(?)
    def _postorder(self, root, max_val):
        if root is None:
            return 0

        count = 0
        if root.val >= max_val:
            count += 1
            max_val = root.val

        return (
            count
            + self._postorder(root.left, max_val)
            + self._postorder(root.right, max_val)
        )

    def goodNodes(self, root: TreeNode) -> int:
        return self._postorder(root, root.val)


# Question URL: https://neetcode.io/problems/count-good-nodes-in-binary-tree/question?list=neetcode150
# Solution: ? -- runtime O(?), space O(?)
