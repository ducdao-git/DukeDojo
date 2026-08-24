from typing import Optional
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution2:  # runtime O(n), space O(n)
    def _inorder(self, root, res=None):
        if res is None:
            res = []

        if not root:
            return res

        if root.left:
            self._inorder(root.left, res)
        res.append(root.val)
        if root.right:
            self._inorder(root.right, res)

        return res

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder_trav = self._inorder(root)

        for i in range(1, len(inorder_trav)):
            if inorder_trav[i] <= inorder_trav[i - 1]:
                return False

        return True


class Solution:  # runtime O(n), space O(1), call-stack O(h)
    def dfs(self, root, low, high):
        if not root:
            return True

        if not (low < root.val < high):
            return False

        return all(
            [self.dfs(root.left, low, root.val), self.dfs(root.right, root.val, high)]
        )

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, -math.inf, math.inf)  # this boundary is from the question


# Question URL: https://neetcode.io/problems/valid-binary-search-tree/question?list=neetcode150
# Solution: binary tree traversal -- runtime O(n), space O(n)
#   Try to travel the tree dfs. After travel, if the result is a sorted list then it is a binary search tree
