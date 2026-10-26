class NumMatrix:
    def __init__(self, matrix: list[list[int]]):  # runtime O(n^2), space O(n^2)
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        # calculate prefix sum of matrix with this number as bottom right conner
        for r in range(ROWS):
            _sum = 0
            for c in range(COLS):
                _sum += matrix[r][c]
                self.prefix_sum[r + 1][c + 1] = _sum + self.prefix_sum[r][c + 1]

    def sumRegion(
        self, row1: int, col1: int, row2: int, col2: int
    ) -> int:  # runtime O(1), space O(1)
        res_bot_right = self.prefix_sum[row2 + 1][col2 + 1]
        # res_top_left = self.prefix_sum[row1 + 1][col1 + 1]
        exclude_top_left = self.prefix_sum[row1][col1]
        exclude_top_right = self.prefix_sum[row1][col2 + 1]
        exclude_bot_left = self.prefix_sum[row2 + 1][col1]

        # Explain: https://neetcode.io/problems/range-sum-query-2d-immutable/solution (3. Two Dimensional Prefix Sum)
        return res_bot_right - exclude_top_right - exclude_bot_left + exclude_top_left


# Question URL: https://neetcode.io/problems/range-sum-query-2d-immutable/question
# Solution: 2D Prefix Sum -- runtime O(1), space O(1)
#   at each pos, is prefix sum of rectangle matrix from (0, 0) to (pos_row, pos_col) -- (pos_row, pos_col) is bottom right of that rectangle matrix
#   => matrix_sum = prefix_sum_at_pos - exclude_prefix_sum_row - exclude_prefix_sum_col + exclude_prefix_sum_top_left
#   must +exclude_prefix_sum_top_left, because -exclude_prefix_sum_row and -exclude_prefix_sum_col both include exclude_prefix_sum_top_left
