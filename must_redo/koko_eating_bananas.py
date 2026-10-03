import math


class Solution:  # runtime O(nlogm), space O(1)
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        max_count = max(piles)
        if h == len(piles):
            return max_count

        min_k, max_k = 1, max_count
        ideal_k = max_count

        while min_k <= max_k:
            mid_k = (min_k + max_k) // 2

            time = 0
            for count in piles:
                time += math.ceil(count / mid_k)

            if time <= h:
                ideal_k = min(mid_k, ideal_k)
                max_k = mid_k - 1
            else:
                min_k = mid_k + 1

        return ideal_k


# Question URL: https://neetcode.io/problems/eating-bananas/question?list=neetcode150
# Solution: binary search -- runtime O(nlogm), space O(1) -- n is the number of elem in piles, m is the maximum value in piles
#   step1: determine min_k is 1 (bcz positive number only), max_k is largest pile (ensure each hour will finish a pile)
#   step2: go through each k value and calculate time take to finish all piles, track smallest k value that allow to finish all piles in h time
#   notes: optimized step 2 with binary search, only calculate time for half of k
#          since calculate time is O(n) op, calculate half of the time will result in O(nlogm)
sol_test = Solution()
print(sol_test.minEatingSpeed(piles=[1, 4, 3, 2], h=9))
