class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        str_map = {}
        for s in strs:
            key = "".join(sorted(s))

            if key in str_map:
                str_map[key].append(s)
            else:
                str_map[key] = [s]

        return list(str_map.values())


test_sol = Solution()
test_strs = ["act", "pots", "tops", "cat", "stop", "hat"]
print(test_sol.groupAnagrams(test_strs))
