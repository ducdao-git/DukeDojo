class Solution2:  # runtime O(n), space O(n)
    def pivotIndex(self, nums: list[int]) -> int:
        prefix_sum = [0]
        postfix_sum = [0]

        _sum = 0
        for n in nums:
            _sum += n
            prefix_sum.append(_sum)

        _sum = 0
        for n in reversed(nums):
            _sum += n
            postfix_sum.append(_sum)

        prefix_sum.pop()
        postfix_sum.pop()
        postfix_sum = postfix_sum[::-1]

        for i in range(len(prefix_sum)):
            if prefix_sum[i] == postfix_sum[i]:
                return i

        return -1


class Solution:  # runtime O(n), space O(1)
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)

        _sum = 0
        for i in range(len(nums)):
            n = nums[i]
            if total - _sum == _sum + n:
                return i
            _sum += n

        return -1


# Question URL: https://neetcode.io/problems/find-pivot-index/question?list=neetcode150
# Solution: Prefix Sum -- runtime O(n), space O(1)
#   Calcualte nums total, at each index, if n is pivot, then left_n_prefix sum = right_n_postfix_sum
#   => total - prev_prefix_sum = prev_prefix_sum + n
sol_test = Solution()
print(sol_test.pivotIndex(nums=[3, 2, 1]))
