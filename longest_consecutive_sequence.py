class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        longest = 0 if not nums else 1

        for n in nums:
            if n - 1 in nums:
                continue

            if n + 1 in nums:
                count = 2
                latest = n + 1

                while latest + 1 in nums:
                    count += 1
                    latest += 1

                longest = max(count, longest)

        return longest


sol_test = Solution()
print(sol_test.longestConsecutive([0]))
