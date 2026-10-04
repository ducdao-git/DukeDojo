class Solution:  # runtime O(logn), space O(1)
    def findMin(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return min(nums)

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] > nums[mid - 1]:
                # nums[mid - 1] < nums[mid] < nums[r]
                r = mid - 1
            else:
                # nums[mid - 1] > nums[mid] < nums[r]
                # can return because nums is in sorted order, thus each elem must be smaller than the one come after it
                return nums[mid]


# Question URL: https://neetcode.io/problems/find-minimum-in-rotated-sorted-array/question?list=neetcode150
# Solution: binary search -- runtime O(logn), space O(1)
#   case1; compare mid to right_end, if mid > right_end, then min will be right of mid (the arr is rotated)
#   case2: if mid < right_end, then min can be on left side or at mid position. like [4, 0, 1, 2, 3] or [3, 4, 0, 1, 2]
sol_test = Solution()
print(sol_test.findMin(nums=[9, -5, -2, 0, 3]))
