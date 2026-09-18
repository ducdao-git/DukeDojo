class Solution:  # runtime O(n), space O(k)
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()  # Cur window of size <= k
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1

            if nums[r] in window:
                return True
            window.add(nums[r])

        return False


# Question URL: https://neetcode.io/problems/contains-duplicate-ii/question?list=neetcode150
# Solution: ? -- runtime O(?), space O(?)
#
sol_test = Solution()
print(sol_test.containsNearbyDuplicate(nums=[2, 1, 2], k=1))
