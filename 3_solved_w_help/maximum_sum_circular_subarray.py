class Solution:  # runtime O(n), space O(1)
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        abs_min = abs_max = nums[0]
        curr_min = curr_max = 0
        total = 0

        for n in nums:
            total += n

            curr_max = max(curr_max, 0) + n
            abs_max = max(abs_max, curr_max)

            curr_min = min(curr_min, 0) + n
            abs_min = min(abs_min, curr_min)

        if abs_max < 0:
            return abs_max

        return max(total - abs_min, abs_max)


# Question URL: https://neetcode.io/problems/maximum-sum-circular-subarray/question
# Solution: Kadane Algo -- runtime O(n), space O(1)
#   we can either find the min_sum or the max_sum at the middle of the array.
#   if we found min_sum in the middle, then max_sum = total - min_sum
#   note - special case:
#       when all value is negative, min_sum = total, result in max_sum = 0. this is not correct, as all values are neg.
#       thus if max_sum < 0, then max_sum = largest_elem in the array, retrun max_sum
sol_test = Solution()
print(sol_test.maxSubarraySumCircular(nums=[-2, -3, -1]))
