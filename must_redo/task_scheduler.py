import heapq
from queue import Queue as q


# # TODO: not yet solve
# class Solution:  # runtime O(?), space O(?)
#     def leastInterval(self, tasks: list[str], n: int) -> int:
#         counter = {}
#         for t in tasks:
#             if t in counter:
#                 counter[t] += 1
#             else:
#                 counter[t] = 1

#         counter_heap = [(-1 * c, t) for t, c in counter.items()]
#         heapq.heapify(counter_heap)

#         result = []
#         queue = q()
#         while counter_heap:
#             counter, task = heapq.heappop(counter_heap)
#             result.append(task)

#             if counter + 1:
#                 queue.put((counter + 1, task))

#             if queue.qsize() == n:
#                 val = queue.get()
#                 if val == "idle":
#                     result.append(val)
#                 else:
#                     heapq.heappush(queue.get())
#             else:
#                 queue.put("idle")

#         return result


# # Question URL:
# # Solution: ? -- runtime O(?), space O(?)
#
# sol_test = Solution()
# print(sol_test.leastInterval(tasks=["X", "X", "Y", "Y"], n=2))
