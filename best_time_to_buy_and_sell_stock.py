class Solution:  # runtime O(n), space O(1)
    def maxProfit(self, prices: list[int]) -> int:
        l = 0
        max_profit = 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
                continue

            max_profit = max(max_profit, prices[r] - prices[l])

        return max_profit


# Question URL: https://neetcode.io/problems/buy-and-sell-crypto/question?list=neetcode150
# Solution: ? -- runtime O(n), space O(1)
#
sol_test = Solution()
print(sol_test.maxProfit(prices=[10, 1, 5, 6, 7, 1]))
