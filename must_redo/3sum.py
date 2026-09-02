def two_sum(numbers: list[int], l_bound, r_bound, target: int) -> list[int]:
    l, r = l_bound, r_bound
    result = []

    while l < r:
        _sum = numbers[l] + numbers[r]

        if _sum == target:
            result.append([numbers[l], numbers[r]])
            l += 1
            r -= 1
        elif _sum < target:
            l += 1
        else:
            r -= 1

    return result


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)

        result = set()
        for i in range(len(nums)):
            n = nums[i]
            if n > 0:
                break  # bcz array is sorted, if 1st elem is positive then no triplet can be eq to 0.

            if i > 0 and n == nums[i - 1]:
                continue

            complement = two_sum(nums, i + 1, len(nums) - 1, 0 - n)
            if not complement:
                continue

            for double in complement:
                result.add(tuple([n] + double))

        return [list(triplet) for triplet in result]


sol_test = Solution()
print(sol_test.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
