class Solution:  # runtime O(n), space O(1)
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0

        for n in nums:
            curr_sum = max(curr_sum, 0) + n
            max_sum = max(max_sum, curr_sum)

        return max_sum


# Question URL: https://neetcode.io/problems/maximum-subarray/question?list=neetcode150
# Solution: ? -- runtime O(?), space O(?)
#
sol_test = Solution()
print(sol_test.maxSubArray())
