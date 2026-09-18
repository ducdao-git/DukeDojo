class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_map = {}
        for n in nums:
            if n in num_map:
                num_map[n] += 1
            else:
                num_map[n] = 1

        output = []
        top_k_freq = set(sorted(num_map.values(), reverse=True)[:k])

        for _k, _v in num_map.items():
            if _v in top_k_freq:
                output.append(_k)

        return output


#! redo other solution with O(n) time and O(n) space.
# Current solution have O(nlogn) time and O(n) space.
