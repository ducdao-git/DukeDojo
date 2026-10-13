class Solution:  # runtime O(?), space O(?)
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        result_row = None

        while not result_row and top <= bot:
            mid = (top + bot) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                result_row = mid if matrix[mid][-1] >= target else None
                top = mid + 1

        if result_row is None:
            return False

        left, right = 0, len(matrix[result_row])
        while left <= right:
            mid = (left + right) // 2

            if matrix[result_row][mid] == target:
                return True
            elif matrix[result_row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


# Question URL:
# Solution: binary search -- runtime O(logm + logn), space O(1)
#   binary search for row that must contain the number based on the 1st elem,
#   then binary search on the row to find if number in ther
sol_test = Solution()
print(
    sol_test.searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3
    )
)
