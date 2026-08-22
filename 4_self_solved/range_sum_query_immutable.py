class NumArray:
    def __init__(self, nums: list[int]):  # runtime O(n), space O(n)
        self.prefix_sum = []
        _sum = 0

        for n in nums:
            _sum += n
            self.prefix_sum.append(_sum)

    def sumRange(self, left: int, right: int) -> int:  # runtime O(1), space O(1)
        pre_right = self.prefix_sum[right]
        pre_left = self.prefix_sum[left - 1] if left > 0 else 0
        return pre_right - pre_left


# Question URL: https://neetcode.io/problems/range-sum-query-immutable/question?list=neetcode150
# Solution: ? -- runtime O(?), space O(?)
