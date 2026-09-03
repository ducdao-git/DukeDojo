class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# use BFS: add all nodes from each layers, skip Null. right side view will be the last node (non-Null) at each layer.
class Solution:  # runtime O(n), space O(n)
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        layer_list = [[root]]

        count = 0
        while True:
            _layer = []
            for n in layer_list[count]:
                if n.left:
                    _layer.append(n.left)
                if n.right:
                    _layer.append(n.right)

            if not _layer:
                break

            layer_list.append(_layer)
            count += 1

        result = []
        for l in layer_list:
            result.append(l[-1].val)

        return result
