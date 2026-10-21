class Solution:  # runtime O(n), space O(1)
    def rob_helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            new_rob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = new_rob

        return rob2

    def rob(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        return max(
            self.rob_helper(nums[1:]),  # exclude last house
            self.rob_helper(nums[:-1]),  # exclude first house
        )


# Question URL: https://neetcode.io/problems/house-robber-ii/question
# Solution: BottomUp DP -- runtime O(n), space O(1)
#   same as house rober 1, but separate into 2 calls:
#   call 1: include first house, exclude last house
#   call 2: exclude first house, include first house
sol_test = Solution()
print(sol_test.rob(nums=[3, 4, 3]))
