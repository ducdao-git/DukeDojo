# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"({self.key}, {self.value})"


class Solution:
    def merge_action(self, sorted_pairs_1, sorted_pairs_2):
        result_list = []
        i, j = 0, 0

        while i < len(sorted_pairs_1) and j < len(sorted_pairs_2):
            if sorted_pairs_1[i].key <= sorted_pairs_2[j].key:
                result_list.append(sorted_pairs_1[i])
                i += 1
            else:
                result_list.append(sorted_pairs_2[j])
                j += 1

        if i < len(sorted_pairs_1):
            result_list.extend(sorted_pairs_1[i:])
        elif j < len(sorted_pairs_2):
            result_list.extend(sorted_pairs_2[j:])

        return result_list

    def mergeSort(self, pairs: list[Pair]) -> list[Pair]:
        list_len = len(pairs)
        if list_len <= 1:
            return pairs

        split_index = list_len // 2
        return self.merge_action(
            self.mergeSort(pairs[:split_index]), self.mergeSort(pairs[split_index:])
        )


test_pairs = [
    Pair(5, "apple"),
    Pair(2, "banana"),
    Pair(9, "cherry"),
    Pair(1, "date"),
    Pair(9, "elderberry"),
]
sol_test = Solution()
print(sol_test.mergeSort(test_pairs))
