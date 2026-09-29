class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            _sum = numbers[l] + numbers[r]
            if _sum == target:
                return [l + 1, r + 1]
            elif _sum < target:
                l += 1
            else:
                r -= 1


sol_test = Solution()
print(sol_test.twoSum(numbers=[-5, -3, 0, 2, 4, 6, 8], target=5))
