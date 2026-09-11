import heapq  # Assuming using python<=3.13 -- only have min-heap


class Solution:  # runtime O(nlogn), space O(1)
    def lastStoneWeight(self, stones: list[int]) -> int:
        # This 'heapify' take O(nlogn) -- top-down
        # stones = []
        # for s in stones:
        #     heapq.heappush(stones, -1 * s)

        # This version of heapify only take O(n) -- bottom up
        stones = [-1 * s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:  # O(n)
            diff = heapq.heappop(stones) - heapq.heappop(stones)  # O(logn)
            if diff:
                heapq.heappush(stones, diff)  # O(logn)

        return -1 * stones[0] if len(stones) else 0


# Question URL: https://neetcode.io/problems/last-stone-weight/question?list=neetcode150
# Solution: ? -- runtime O(?), space O(?)
#
sol_test = Solution()
print(sol_test.lastStoneWeight(stones=[2, 3, 6, 2, 4]))
