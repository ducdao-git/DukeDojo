class Solution:  # runtime O(n), space O(1)
    def removeDuplicates(self, nums: list[int]) -> int:
        l = r = 0

        while r < len(nums):
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                count += 1
                r += 1

            for _ in range(min(2, count)):
                nums[l] = nums[r]
                l += 1

            r += 1

        return l


# Question URL: https://neetcode.io/problems/remove-duplicates-from-sorted-array-ii/question?list=neetcode150
# Solution: ? -- runtime O(?), space O(?)
#
sol_test = Solution()
print(sol_test.removeDuplicates(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3]))
