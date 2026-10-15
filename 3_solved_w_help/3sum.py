class Solution:  # runtime O(n^2), space O(m)
    def two_sum(self, nums, l, r, target):
        result = []

        while l < r:
            _sum = nums[l] + nums[r]
            if _sum > target:
                r -= 1
            elif _sum < target:
                l += 1
            else:
                result.append([nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1

        return result

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # O(nlogn)
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            n = nums[i]

            other_2 = self.two_sum(nums, i + 1, len(nums) - 1, 0 - n)

            if not other_2:
                continue

            for pair in other_2:
                result.append([n, *pair])

        return result


# Question URL: https://neetcode.io/problems/three-integer-sum/question?list=neetcode150
# Solution: 2 pointers -- runtime O(n^2), space O(1)
#   Sort array, for each elem, run 2sum on all elems come after it. Skip repeated elems
sol_test = Solution()
print(sol_test.threeSum(nums=[0, 0, 0]))
