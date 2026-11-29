class Solution:  # runtime O(n^2), space O(n)
    def helper(self, i, nums, curr_set, return_set):
        if i == len(nums):
            return_set.append(curr_set.copy())
            return

        # decision to include the number
        curr_set.append(nums[i])
        self.helper(i + 1, nums, curr_set, return_set)

        # decision to not include the number
        curr_set.pop()
        self.helper(i + 1, nums, curr_set, return_set)

    def subsets(self, nums: list[int]) -> list[list[int]]:
        curr_set, return_set = [], []
        self.helper(0, nums, curr_set, return_set)
        return return_set


# Question URL: https://neetcode.io/problems/subsets/question?list=neetcode150
# Solution: Backtracking -- runtime O(n^2), space O(n)
#
sol_test = Solution()
print(sol_test.subsets(nums=[1, 2, 3]))
