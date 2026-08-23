class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid

        return -1


sol_test = Solution()
print(sol_test.search(nums=[1, 3, 3, 3, 3, 3, 3, 4, 6, 6, 7, 8, 9], target=3))
