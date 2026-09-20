class Solution2:  # runtime avg O(n), space O(1)
    def removeDuplicates(self, nums: list[int]) -> int:
        # forced 2 pointers solution
        i = 0
        j = i + 1

        while j < len(nums):
            if nums[j] != nums[i]:
                i = j
                j += 1
            else:
                nums.pop(j)

        return len(nums)


class Solution:  # runtime O(n), space O(1)
    def removeDuplicates(self, nums: list[int]) -> int:
        i = j = 1

        while j < len(nums):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
            j += 1

        return i


# Question URL: https://neetcode.io/problems/remove-duplicates-from-sorted-array/question?list=neetcode150
# Solution: 2 pointers -- runtime O(n), space O(1)
#   l pointer keep track elem can be replace, r pointer move forward and check
#   if it diff from the one right infront of it (because arr is sorted)
sol_test = Solution()
print(sol_test.removeDuplicates(nums=[1, 1, 2, 3, 4]))
