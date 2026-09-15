from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:  # runtime O(k), space O(k)
    def _inorder(self, tree_node, nums, k):
        if not tree_node or len(nums) >= k:
            return nums

        self._inorder(tree_node.left, nums, k)
        nums.append(tree_node.val)
        self._inorder(tree_node.right, nums, k)

        return nums

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self._inorder(root, [], k)[k - 1]


# Question URL: https://neetcode.io/problems/kth-smallest-integer-in-bst/question
# Solution: ? -- runtime O(k), space O(k)
#
sol_test = Solution()
print(sol_test.kthSmallest())
