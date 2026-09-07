import heapq
import math


class Solution:  # runtime O(n+klogn), space O(n)
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        if k == len(points):
            return points

        dis_point_map = {}
        for p in points:
            dis = math.sqrt((p[0]) ** 2 + (p[1]) ** 2)
            if dis in dis_point_map:
                dis_point_map[dis].append(p)
            else:
                dis_point_map[dis] = [p]

        _keys = list(dis_point_map)
        heapq.heapify(_keys)

        result = []
        while len(result) < k:
            result.extend(dis_point_map[heapq.heappop(_keys)])
        return result[:k]


# Question URL: https://neetcode.io/problems/k-closest-points-to-origin/question
# Solution: heap -- runtime O(n+klogn), space O(n) -- n is number of point, k is number of return point
#   Step1: Loop thru all points to calculate is distance O(n)
#   Step2: Min-heap the distances O(n)
#   Step3: Keep heap pop until get k-nearest point O(klogn)
sol_test = Solution()
print(sol_test.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2))
