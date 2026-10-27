class Solution:  # runtime O(n), space O(1)
    def findDuplicate(self, nums: list[int]) -> int:
        # !!! Let len(nums)=n, each integer in nums is in the range [1, n] inclusive
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                # meet point of fast & slow is not duplicate number
                # meet point only confirm there are cycle
                break

        # find head of cycle (our duplicate number)
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow


# Question URL:
# Solution: Fast & Slow Pointer -- runtime O(n), space O(1)
#   very tricky, idea is treat value at each curr position is the index of the next position
#   in other words, position value is pointer to next position
sol_test = Solution()
print(sol_test.FUNC_NAME())
