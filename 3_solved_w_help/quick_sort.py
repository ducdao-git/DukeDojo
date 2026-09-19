# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value


class Solution:
    def quick_sort_helper(self, arr, start_index, end_index):
        print(arr, start_index, end_index)
        if (end_index - start_index + 1) <= 1:
            return arr

        tobe_swap_index = start_index
        pivot_index = end_index
        pivot_val = arr[pivot_index]

        for i in range(start_index, end_index):
            if arr[i] <= pivot_val:
                temp = arr[tobe_swap_index]
                arr[tobe_swap_index] = arr[i]
                arr[i] = temp
                tobe_swap_index += 1

        temp = arr[tobe_swap_index]
        arr[tobe_swap_index] = arr[pivot_index]
        arr[pivot_index] = temp

        self.quick_sort_helper(arr, start_index, tobe_swap_index - 1)
        self.quick_sort_helper(arr, tobe_swap_index + 1, end_index)

        return arr

    def quickSort(self, pairs: list[int]) -> list[int]:
        return self.quick_sort_helper(pairs, 0, len(pairs) - 1)


test_pairs = [3, 1, 6, 9, 8, 5, 12, 16, 18, 12, 50, 36, 40, 25]
sol_test = Solution()
print(sol_test.quickSort(test_pairs))
