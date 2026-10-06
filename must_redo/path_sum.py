# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def has_path_sum_helper(self, root, path, path_sum, target_sum):
        if not root:
            return False

        path.append(root.val)
        path_sum += root.val

        if not root.left and not root.right:
            if path_sum == target_sum:
                return True
            else:
                path.pop()
                path_sum -= root.val
                return False

        if self.has_path_sum_helper(root.left, path, path_sum, target_sum):
            return True

        if self.has_path_sum_helper(root.right, path, path_sum, target_sum):
            return True

        path.pop()
        path_sum -= root.val

        return False

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.has_path_sum_helper(root, [], 0, targetSum)
