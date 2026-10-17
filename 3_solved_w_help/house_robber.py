from typing import Optional


class Solution2:  # runtime O(n), space O(n)
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        memo = {0: nums[0], 1: max(nums[0], nums[1])}

        def helper(i):
            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + helper(i - 2), helper(i - 1))
            return memo[i]

        return helper(n - 1)


class Solution:  # runtime O(n), space O(1)
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)

        dp = [nums[0], max(nums[0], nums[1])]

        for i in range(2, n):
            temp = dp[0]
            dp[0] = dp[1]
            dp[1] = max(nums[i] + temp, dp[0])

        return dp[1]


# Question URL: https://neetcode.io/problems/house-robber/history?list=neetcode150&submissionIndex=2
# Solution: BottomUp DP -- runtime O(n), space O(1)
#   At each i, we can either rob the house or not rob it. So at i, the max we can rob is:
#       house[i] = max(max(house[i-1]), house[i] + max(house[i-2]))
#   We only need to keep track the max we can rob at house[i-1] and house[i-2], thus space is O(1)
sol_test = Solution()
print(
    sol_test.rob(
        nums=[
            1,
            3,
            5,
            7,
            9,
            11,
            13,
            15,
            17,
            19,
            2,
            4,
            6,
            8,
            10,
            12,
            14,
            16,
            18,
            20,
            21,
            23,
            25,
            27,
            29,
            31,
            33,
            35,
            37,
            39,
            40,
            42,
            44,
            46,
            48,
            50,
            52,
            54,
            56,
            58,
            60,
            62,
            64,
            66,
            68,
            70,
            72,
            74,
            76,
            78,
            80,
            82,
            84,
            86,
            88,
            90,
            92,
            94,
            96,
            98,
            100,
            99,
            97,
            95,
            93,
            91,
            89,
            87,
            85,
            83,
            81,
            79,
            77,
            75,
            73,
            71,
            69,
            67,
            65,
            63,
            61,
            59,
            57,
            55,
            53,
            51,
            49,
            47,
            45,
            43,
            41,
            39,
            37,
            35,
            33,
            31,
            29,
            27,
            25,
            23,
        ]
    )
)
