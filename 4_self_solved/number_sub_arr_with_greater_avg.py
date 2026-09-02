from collections import deque


class Solution:  # runtime O(n), space O(k)
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        window = deque()
        window_sum, count, l = 0, 0, 0

        for r in range(len(arr)):
            if r - l + 1 > k:
                # remove most left whenever window size > k
                window.popleft()
                window_sum -= arr[l]
                l += 1

            window.append(arr[r])
            window_sum += arr[r]

            if len(window) == k:
                count += 1 if window_sum / k >= threshold else 0

        return count


# Question URL: https://neetcode.io/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/question?list=neetcode150
# Solution: FixedS Window -- runtime O(n), space O(k)
#
sol_test = Solution()
print(sol_test.numOfSubarrays(arr=[2, 2, 2, 2, 5, 5, 5, 8], k=3, threshold=4))
