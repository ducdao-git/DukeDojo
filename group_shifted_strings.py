# wrap around, use mod: (ord(b) - ord(a)) % 26 + ord(a) = ord(b)


class Solution:
    def get_hash_str(self, s):
        normalized_diff = ord(s[0]) % ord("a")

        hashed_chars = []
        for ch in s:
            # can replace next 3 lines with: ord(<ch+1>) - ord(<ch>) % 26
            hash_val = ord(ch) - normalized_diff
            if hash_val < 97:
                hash_val = 122 - (97 - hash_val - 1)

            hash_char = chr(hash_val)
            hashed_chars.append(hash_char)

        return "".join(hashed_chars)

    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        group_map = {}
        for s in strings:
            key = self.get_hash_str(s)
            if key in group_map:
                group_map[key].append(s)
            else:
                group_map[key] = [s]

        return list(group_map.values())


sol_test = Solution()
test_strings = ["fpbnsbrkbcyzdmmmoisaa", "rbnzendwnoklpyyyauemm"]
print(sol_test.groupStrings(test_strings))
