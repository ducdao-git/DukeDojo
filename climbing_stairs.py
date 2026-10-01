class Solution:
    result_db = {
        1: 1,
        2: 2,
    }

    def climbStairs(self, n: int) -> int:
        if n in self.result_db:
            return self.result_db[n]
        else:
            self.result_db[n] = self.climbStairs(n - 2) + self.climbStairs(n - 1)

        return self.result_db[n]


sol_test = Solution()
print(sol_test.climbStairs(38))
