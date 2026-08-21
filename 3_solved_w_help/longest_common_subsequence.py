class Solution2:  # runtime O(mn), space O(mn)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLS = len(text1), len(text2)
        cache = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in reversed(range(ROWS)):
            for c in reversed(range(COLS)):
                if text1[r] == text2[c]:
                    cache[r][c] = 1 + cache[r + 1][c + 1]
                else:
                    cache[r][c] = max(cache[r + 1][c], cache[r][c + 1])

        print(*cache, sep="\n")
        return cache[0][0]


class Solution:  # runtime O(mn), space O(n)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLS = len(text1), len(text2)
        prev_row = [0] * (COLS + 1)

        for r in reversed(range(ROWS)):
            curr_row = [0] * (COLS + 1)

            for c in reversed(range(COLS)):
                if text1[r] == text2[c]:
                    curr_row[c] = 1 + prev_row[c + 1]
                else:
                    curr_row[c] = max(prev_row[c], curr_row[c + 1])

            prev_row = curr_row

        return prev_row[0]


# Question URL: https://neetcode.io/problems/longest-common-subsequence/question
# Solution: BottomUp DP -- runtime O(mn), space O(n)
#   imagine len(text1)xlen(text2) grid, return value at cell[0][0]
#   if 2 chars match, value at cell is: 1 + diagonal (down+right) cell value
#   if 2 chars not match, value at cell is: max(down_cell, right_cell)
sol_test = Solution()
print(sol_test.longestCommonSubsequence(text1="crabt", text2="car"))
