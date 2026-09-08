class Solution:  # runtime O(n), space O(1)
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = curr_sum = 0
        length = float("inf")

        for r in range(len(nums)):
            curr_sum += nums[r]

            while curr_sum >= target:
                length = min(length, r - l + 1)
                curr_sum -= nums[l]
                l += 1

        return 0 if length > len(nums) else length


# Question URL: https://neetcode.io/problems/minimum-size-subarray-sum/question?list=neetcode150
# Solution: VariableS Window -- runtime O(n), space O(1)
#   loop r thru the list, if sum of window >= target, increase l until the sum < target
sol_test = Solution()
print(sol_test.minSubArrayLen(target=10, nums=[2, 1, 5, 1, 5, 3]))
