from collections import deque


class Solution:  # runtime O(?), space O(?)
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        lands = set()
        max_area = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    lands.add((r, c))

        if not len(lands):
            return 0

        while lands:
            queue = deque()
            queue.append(lands.pop())

            area = 1
            while queue:
                r, c = queue.pop()

                for dr, dc in DIRECTIONS:
                    _r = r + dr
                    _c = c + dc

                    if (
                        min(_r, _c) < 0
                        or _r == ROWS
                        or _c == COLS
                        or (_r, _c) not in lands
                        or grid[_r][_c] == 0
                    ):
                        continue

                    queue.append((_r, _c))
                    lands.remove((_r, _c))
                    area += 1

            max_area = max(area, max_area)

        return max_area


# Question URL: https://neetcode.io/problems/max-area-of-island/question?list=neetcode150
# Solution: ? -- runtime O(?), space O(?)
#
sol_test = Solution()
print(
    sol_test.maxAreaOfIsland(
        grid=[[0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 0, 0, 1]]
    )
)
