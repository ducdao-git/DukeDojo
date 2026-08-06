# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:  # runtime O(n), space O(1)
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# Question URL: https://neetcode.io/problems/linked-list-cycle-detection/question?list=neetcode150
# Solution: Fast & Slow Pointer -- runtime O(n), space O(1)
#   fast pointer move twice as fast as slow pointer, slow=fast iff cycle exist
