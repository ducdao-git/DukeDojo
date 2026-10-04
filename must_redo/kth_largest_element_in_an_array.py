import heapq


class Solution:  # runtime O(nlogk), space O(n)
    def findKthLargest(self, nums: list[int], k: int) -> int:
        result = nums[:k]
        heapq.heapify(result)  # O(n) time

        # (n-k)logk time
        for i in range(k, len(nums)):
            if nums[i] > result[0]:
                heapq.heapreplace(result, nums[i])
            continue

        return result[0]  # or just heapq.nlargest(k, nums)[-1]


# Question URL: https://neetcode.io/problems/kth-largest-element-in-an-array/question?list=neetcode150
# Solution: min-heap -- runtime O(nlogk), space O(n)
#   min-heap the first k elem
#   scan thru the rest, if elem larger than root min heap, then push elem on that heap
#   effectivly keep track k largest elems
# TODO: redo in O(n) time, O(n) space
sol_test = Solution()
print(sol_test.findKthLargest(nums=[2, 3, 1, 1, 5, 6, 6, 4], k=4))
