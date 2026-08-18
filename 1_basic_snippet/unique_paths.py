class Solution2:  # runtime O(mn), space O(mn)
    def unique_paths(self, r, c, ROWS, COLS, cache):
        if r == ROWS or c == COLS:
            return 0
        if cache[r][c] > 0:
            return cache[r][c]
        if r == ROWS - 1 and c == COLS - 1:
            return 1

        down = self.unique_paths(r + 1, c, ROWS, COLS, cache)
        right = self.unique_paths(r, c + 1, ROWS, COLS, cache)
        cache[r][c] = down + right

        return cache[r][c]

    def uniquePaths(self, m: int, n: int) -> int:
        return self.unique_paths(0, 0, m, n, [[0] * n for _ in range(m)])


class Solution:  # runtime O(mn), space O(n)
    def uniquePaths(self, m: int, n: int) -> int:
        prev_row = [1] * n

        for r in range(m - 2, -1, -1):
            curr_row = [0] * n
            curr_row[-1] = 1

            for c in range(n - 2, -1, -1):
                curr_row[c] = curr_row[c + 1] + prev_row[c]

            prev_row = curr_row

        return prev_row[0]


# Question URL: https://neetcode.io/problems/count-paths/question?list=neetcode150
# Solution: BottomUp PD -- runtime O(mn), space O(n)
#   All value of bottom row is 1, all value of last colume is 1, because we can only go down and right.
#   All other value is calculated based on `curr_row[c + 1] + prev_row[c]`
sol_test = Solution()
print(sol_test.uniquePaths(m=3, n=6))
