class Solution:  # runtime O(n), space O(k)
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = length = 0
        unique_str = set()

        curr_len = 0
        for r in range(len(s)):
            ch = s[r]

            while ch in unique_str:
                unique_str.remove(s[l])
                l += 1
                curr_len -= 1

            unique_str.add(ch)
            curr_len += 1
            length = max(length, curr_len)

        return length


# Question URL: https://neetcode.io/problems/longest-substring-without-duplicates/question?list=neetcode150
# Solution: VariableS Window -- runtime O(n), space O(k)
#   loop r thru the string, keep increase curr len. until hit a duplicate, move l, down size the window until the duplicate is remove
sol_test = Solution()
print(sol_test.lengthOfLongestSubstring(s="  "))
