from collections import deque


class Solution:  # runtime O(nm), space O(nm)
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue = deque()
        # rottens = set()

        # get all the init rottens
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    # rottens.add((r, c))

        # rotten fruits affect all neighbor fruits in the next min
        minute = 0
        while queue:
            minute += 1

            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in DIRECTIONS:
                    _r = r + dr
                    _c = c + dc

                    if (
                        min(_r, _c) < 0
                        or _r == ROWS
                        or _c == COLS
                        or grid[_r][_c] == 0
                        or grid[_r][_c] == 2  # or (_r, _c) in rottens
                    ):
                        continue

                    queue.append((_r, _c))
                    grid[_r][_c] = 2  # rottens.add((_r, _c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:  # and (r, c) not in rottens:
                    return -1

        # cuz last while loop will check if current rottens in the queue effect any other.
        #  but there are no others connected fruit, so no others will be rotten.
        #  hence all fruit are rotten at time-1
        return max(0, minute - 1)


# Question URL: https://neetcode.io/problems/rotting-fruit/question?list=neetcode150
# Solution: matrix bfs -- runtime O(nm), space O(nm)
#   from each rotten fruit, all fruits around it get rotten in the next min, add all these surround fruits to queue.
#   while there are rotten fruits in queue, check if it can affect it's neighbors
sol_test = Solution()
print(sol_test.orangesRotting(grid=[[1, 1, 0], [0, 1, 1], [0, 1, 2]]))
