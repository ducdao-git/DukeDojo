class Solution:
    def maxArea(self, heights: list[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            hgl, hgr = heights[l], heights[r]

            area = (r - l) * min(hgl, hgr)
            max_area = max(area, max_area)

            if hgl < hgr:
                while l < r and heights[l] <= hgl:
                    l += 1
            else:
                while l < r and heights[r] <= hgr:
                    r -= 1

        return max_area


# Question URL: https://neetcode.io/problems/max-water-container/question?list=neetcode150
#   2 pointers, max area bounded by height of min col and width.
#   As width get closer, area only bigger if min col is higher
sol_test = Solution()
print(sol_test.maxArea(heights=[1, 7, 2, 5, 4, 7, 3, 6]))
