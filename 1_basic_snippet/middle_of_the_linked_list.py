from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:  # runtime O(n), space O(1)
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


# Question URL: https://neetcode.io/problems/middle-of-the-linked-list/question?list=neetcode150
# Solution: Fast & Slow Pointer -- runtime O(n), space O(1)
