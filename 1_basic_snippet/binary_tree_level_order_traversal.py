# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []

        tbp_node = 1
        level_order = [[root]]

        while tbp_node > 0:
            prev_level = level_order[-1]
            curr_level = []

            for node in prev_level:
                tbp_node -= 1
                if not node:
                    continue

                curr_level.extend([node.left, node.right])
                tbp_node += 2

            if curr_level:
                level_order.append(curr_level)

        # Convert node to value
        result_order = []
        for level in level_order:
            _level = []

            for node in level:
                if node:
                    _level.append(node.val)

            if _level:
                result_order.append(_level)

        return result_order
