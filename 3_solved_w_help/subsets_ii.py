class Solution:  # runtime O(n^2), space O(n)
    def helper(self, i, nums, curr_set, return_set):
        if i == len(nums):
            return_set.append(curr_set.copy())
            return

        # decision to include num
        curr_set.append(nums[i])
        self.helper(i + 1, nums, curr_set, return_set)

        # skip all duplicate nums
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1

        # decision to not include num
        curr_set.pop()
        self.helper(i + 1, nums, curr_set, return_set)

    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        curr_set, return_set = [], []
        self.helper(0, nums, curr_set, return_set)
        return return_set


# Question URL: https://neetcode.io/problems/subsets-ii/question?list=neetcode150
# Solution: Backtracking -- runtime O(n^2), space O(n)
#
sol_test = Solution()
print(sol_test.subsetsWithDup(nums=[1, 2, 1]))
