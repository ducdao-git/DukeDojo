from collections import deque


class Solution:  # runtime O(nm), space O(nm)
    def numIslands(self, grid: list[list[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        lands = set()
        for _r in range(ROWS):
            for _c in range(COLS):
                if grid[_r][_c] == "1":
                    lands.add((_r, _c))

        islands = 0
        while lands:
            r, c = lands.pop()

            queue = deque()
            queue.append((r, c))

            print(lands)
            print(queue)
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
                    ):
                        continue

                    queue.append((_r, _c))
                    lands.remove((_r, _c))

            islands += 1

        return islands


# Question URL: https://neetcode.io/problems/count-number-of-islands/question?list=neetcode150
# Solution: Matrix BFS -- runtime O(nm), space O(nm)
#   keep track all the lands encountered, whenever we encounter a land, we sink all connected lands => this is an island
#   once all lands are sinked, return number of islands
#   can also solve with Matrix DFS
sol_test = Solution()
print(
    sol_test.numIslands(
        grid=[
            ["0", "1", "1", "1", "0"],
            ["0", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
