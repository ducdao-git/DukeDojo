from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root, _sum, target):
        if not root:
            return False

        _sum += root.val
        if not root.left and not root.right:
            return _sum == target

        if self.dfs(root.left, _sum, target):
            return True

        return self.dfs(root.right, _sum, target)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root, 0, targetSum)


# Question URL: https://neetcode.io/problems/path-sum/question
# Solution: backtrack -- runtime O(n), space O(h)
