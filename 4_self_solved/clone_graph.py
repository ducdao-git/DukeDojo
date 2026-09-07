from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:  # runtime O(n), space O(n)
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        graph = {}
        graph[node.val] = []

        queue = deque()
        queue.append(node)

        largest = 0
        while queue:
            n = queue.pop()
            largest = max(largest, n.val)

            for nb in n.neighbors:
                if nb.val not in graph:
                    graph[nb.val] = []
                    queue.append(nb)

                graph[n.val].append(nb.val)

        node_map = {}
        for n in graph:
            node_map[n] = Node(n)

        for n in node_map:
            node_map[n].neighbors = [node_map[i] for i in graph[n]]

        return node_map[1]


# Question URL: https://neetcode.io/problems/clone-graph/history?list=neetcode150&submissionIndex=0
# Solution: ? -- runtime O(?), space O(?)
# Notes: no need to redo
sol_test = Solution()
print(sol_test.FUNC_NAME())
