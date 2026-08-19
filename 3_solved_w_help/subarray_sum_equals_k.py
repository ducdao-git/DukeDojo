class Solution:  # runtime O(n), space O(n)
    def subarraySum(self, nums: list[int], k: int) -> int:
        _sum = 0
        prefix_sum = []

        for n in nums:
            _sum += n
            prefix_sum.append(_sum)

        sum_counter = {0: 1}
        result = 0

        for p in prefix_sum:
            diff = p - k
            if diff in sum_counter:
                result += sum_counter[diff]

            # only count prefix_sum after done process it.
            # avoid example: curr_prefix_sum=2, k=4, then if cout before process, then 2+2=4, thus result+=1
            if p in sum_counter:
                sum_counter[p] += 1
            else:
                sum_counter[p] = 1

        return result


# Question URL: https://neetcode.io/problems/subarray-sum-equals-k/question?list=neetcode150
# Solution: Prefix Sum -- runtime O(n), space O(n)
#   subarray_sum = last_prefix_sum - start-1_prefix_sum. So at any given prefix_sum, let diff=prefix_sum-k,
#   if diff eq to a prior prefix_sum, then result+=occurance_count_of_that_prefix_sum
sol_test = Solution()
print(sol_test.subarraySum(nums=[-1, -1, 1], k=0))
