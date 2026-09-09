class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # right_pass = [nums[0]]
        # for n in nums[1:]:
        #     right_pass.append(n * right_pass[-1])

        # left_pass = [nums[-1]]
        # for n in nums[-2::-1]:
        #     left_pass.append(n * left_pass[-1])
        # left_pass = left_pass[::-1]

        # result = []
        # for i in range(len(nums)):
        #     r = 1 if i - 1 < 0 else right_pass[i - 1]
        #     l = 1 if i + 1 >= len(left_pass) else left_pass[i + 1]
        #     result.append(r * l)

        # return result

        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


test_nums = [1, 2, 4, 6]
sol_test = Solution()
print(sol_test.productExceptSelf(test_nums))
