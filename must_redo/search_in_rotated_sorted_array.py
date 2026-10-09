class Solution:  # runtime O(logn), space O(1)
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # right sorted portion
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


# Question URL: https://neetcode.io/problems/find-target-in-rotated-sorted-array/question
# Solution: binary search -- runtime O(logn), space O(1)
#   since the array is sorted but rotated, picking any mid will result in a left sorted portion, a right sorted portion, or both
#   we only consider the sorted potion,
#       if mid in there, then we move the left and right bound to that portion only
#       if mid not in there, then we move the left and right bound to the other portion (unsorted portion)
sol_test = Solution()
print(sol_test.search(nums=[1], target=0))
