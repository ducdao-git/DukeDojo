class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        temp_stack = []

        for i, t in enumerate(temperatures):
            while temp_stack and t > temp_stack[-1][0]:
                lower_temp = temp_stack.pop()
                result[lower_temp[1]] = i - lower_temp[1]

            temp_stack.append((t, i))

        return result


## Question URL: https://neetcode.io/problems/daily-temperatures/question
# - use stack to store temp, keep pop stack whenever a temp is higher than temp at top stack
# - bcz we keep popping stack until the curr temp not larger that the past temp (or empty),
#     we make sure stack is alw in a sorted order (large->small) where top stack is the smallest temp
sol_test = Solution()
print(sol_test.dailyTemperatures(temperatures=[5, 1]))
