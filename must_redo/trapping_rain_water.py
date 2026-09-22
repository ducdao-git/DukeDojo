class Solution:
    def trap(self, height: list[int]) -> int:
        water = 0
        l, r = 0, len(height) - 1
        max_left = height[l]
        max_right = height[r]

        while l < r:
            if height[l] <= height[r]:
                water += max(max_left - height[l], 0)
                max_left = max(height[l], max_left)
                l += 1
            else:
                water += max(max_right - height[r], 0)
                max_right = max(height[r], max_right)
                r -= 1

        return water


## Question URL: https://neetcode.io/problems/trapping-rain-water/question?list=neetcode150
# - trapped_water[i] = min(left_col, right_col) - col_height[i]
# - since we only need min of left/right col, use 2 pointer and only advance lower height
#    as water is guarantee to trap between lower col and the higher col pointed at by other pointer
sol_test = Solution()
print(sol_test.trap(height=[0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))
