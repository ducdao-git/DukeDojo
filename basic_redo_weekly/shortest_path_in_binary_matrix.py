from collections import deque


class Solution:  # runtime O(n^2), space O(n^2)
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            # both of this must be 0
            return -1

        N = len(grid)  # problem specified this is an n by n matrix
        DIRECTIONS = [
            (0, 1),
            (0, -1),
            (1, 0),
            (1, 1),
            (1, -1),
            (-1, 0),
            (-1, 1),
            (-1, -1),
        ]

        r, c = 0, 0
        queue = deque()
        queue.append((r, c))

        step = 0
        checked = set()

        while queue:
            step += 1

            for _ in range(len(queue)):
                r, c = queue.popleft()

                if r == c == N - 1:
                    return step

                checked.add((r, c))

                for dr, dc in DIRECTIONS:
                    _r = r + dr
                    _c = c + dc

                    if (
                        min(_r, _c) < 0
                        or max(_r, _c) == N
                        or grid[_r][_c] == 1
                        or (_r, _c) in checked
                    ):
                        continue

                    queue.append((_r, _c))

        return -1


# Question URL: https://neetcode.io/problems/shortest-path-in-binary-matrix/question?list=neetcode150
# Solution: Matrix BFS -- runtime O(n^2), space O(n^2)
#   using matrix bfs to explore layer by layer, we check each node 1 once, and at each node
#   we add the 8 surrounding nodes to a queue to be explore. n^2 because we visit each node
#   one in an n by n matrix
sol_test = Solution()
print(sol_test.shortestPathBinaryMatrix(grid=[[0, 1, 0], [1, 0, 0], [1, 1, 0]]))
