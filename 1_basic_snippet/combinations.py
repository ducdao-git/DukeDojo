class Solution2:  # runtime O(k * 2^n), space O(n)
    def helper(self, i, curr_set, result_set, n, k):
        if len(curr_set) == k:
            result_set.append(curr_set.copy())
            return

        if i > n:
            return

        # decision to include it
        curr_set.append(i)
        self.helper(i + 1, curr_set, result_set, n, k)

        # decision to not include it
        curr_set.pop()
        self.helper(i + 1, curr_set, result_set, n, k)

    def combine(self, n: int, k: int) -> list[list[int]]:
        curr_set, result_set = [], []
        self.helper(1, curr_set, result_set, n, k)
        return result_set


class Solution:  # runtime O(k * C(n, k)), space O(n)
    def helper(self, i, curr_set, result_set, n, k):
        if len(curr_set) == k:
            result_set.append(curr_set.copy())
            return

        if i > n:
            return

        for j in range(i, n + 1):  # each node have (n-i) children
            curr_set.append(j)
            self.helper(j + 1, curr_set, result_set, n, k)
            curr_set.pop()

    def combine(self, n: int, k: int) -> list[list[int]]:
        curr_set, result_set = [], []
        self.helper(1, curr_set, result_set, n, k)
        return result_set


# Question URL: https://neetcode.io/problems/combinations/question
# Solution: ? -- runtime O(k * C(n, k)), space O(n)
#
sol_test = Solution()
print(sol_test.combine(n=3, k=2))
