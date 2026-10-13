from typing import Optional
import heapq
from collections import deque


class Solution:  # runtime O(nlog26), space O(n)
    def leastInterval(self, tasks: list[str], n: int) -> int:
        task_counter = {}
        for t in tasks:
            if t in task_counter:
                task_counter[t] += 1
            else:
                task_counter[t] = 1

        task_counter = [[-1 * c, t] for t, c in task_counter.items()]
        heapq.heapify(task_counter)  # O(n)

        result = []
        wait_queue = deque()

        cycle = 0
        while task_counter or wait_queue:
            cycle += 1

            if task_counter:
                c, t = heapq.heappop(task_counter)  # O(logn)
                result.append(t)
                if c + 1 < 0:
                    # task appear at this cycle, and only should reappear after n cycle has passed
                    wait_queue.append([c + 1, t, cycle + n])
            else:
                result.append(None)

            if wait_queue and wait_queue[0][2] == cycle:
                c, t, _ = wait_queue.popleft()
                heapq.heappush(task_counter, [c, t])

        print(result)
        return len(result)


# Question URL: https://neetcode.io/problems/task-scheduling/question?list=neetcode150
# Solution: heap and queue -- runtime O(n), space O(n) -- actual runtime is O(nlog26)
#   resolve most occurence task first with heap. if there are still occurance of task, add to queue.
#   only pop from queue and add back to heap if n cycle has pass for the first element in queue
sol_test = Solution()
print(sol_test.leastInterval(tasks=["X", "X", "X", "Y", "Y"], n=2))
