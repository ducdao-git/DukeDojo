class Solution:  # runtime O(mn), space O(1)
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[-1][-1]:
            return 0

        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        last_row = obstacleGrid[-1]
        last_row[-1] = 1

        for c in range(COLS - 2, -1, -1):
            if last_row[c] == 1:
                last_row[c] = 0
            else:
                last_row[c] = last_row[c + 1]

        prev_row = last_row
        for r in range(ROWS - 2, -1, -1):
            curr_row = obstacleGrid[r]
            curr_row[-1] = 0 if curr_row[-1] else prev_row[-1]

            for c in range(COLS - 2, -1, -1):
                if curr_row[c]:
                    curr_row[c] = 0
                else:
                    curr_row[c] = curr_row[c + 1] + prev_row[c]

            prev_row = curr_row

        return obstacleGrid[0][0]


# Question URL: https://neetcode.io/problems/unique-paths-ii/question?list=neetcode150
# Solution: BottomUp DP -- runtime O(mn), space O(1)
#   like unique path, but whenever a value already exist at cell, mean there is obstacle at that cell, thus cell is eq to 0
#   this problem can only done by bottom up dp, top down dp will result in miss cal as some cell alrd have value 1 (sort of)
sol_test = Solution()
print(sol_test.uniquePathsWithObstacles(obstacleGrid=[[0, 0], [0, 1]]))
