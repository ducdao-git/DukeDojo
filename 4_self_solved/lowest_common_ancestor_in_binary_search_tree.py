class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Question URL: https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree/question?list=neetcode150
class Solution:  # runtime O(h), space O(1) -- h is height of binary tree
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        low, high = p.val, q.val
        if p.val > q.val:
            low, high = q.val, p.val

        while root:
            if high < root.val:
                root = root.left
            elif low > root.val:
                root = root.right
            else:  # low <= root_val <= high:
                return root
