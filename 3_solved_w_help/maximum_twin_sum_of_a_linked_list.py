from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution2:  # runtime O(n), space O(n)
    def pairSum(self, head: Optional[ListNode]) -> int:
        # because linked list len is even, and we want mid point to be the left point, thus fast need to start at slow+1
        # example: linked_list_len=4, if want mid point at index 1, then slow_index=0 and fast_index=1
        slow, fast = head, head.next

        half_list = []
        half_list.append(slow.val)

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            half_list.append(slow.val)

        max_sum = 0
        while half_list:
            slow = slow.next
            _sum = half_list.pop() + slow.val
            max_sum = max(max_sum, _sum)

        return max_sum


class Solution:  # runtime O(n), space O(1)
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            fast = fast.next.next

            # reverse pointer for curr node, then move slow pointer fwd
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        max_sum = 0
        while prev:
            max_sum = max(max_sum, prev.val + slow.val)
            prev = prev.next
            slow = slow.next

        return max_sum


# Question URL: https://neetcode.io/problems/maximum-twin-sum-of-a-linked-list/question?list=neetcode150
# Solution: Fast & Slow Pointer -- runtime O(n), space O(1)
#   In 1 pass, figure out mid point and reverse the first half of the linked list.
#   max_sum will be calculated from middle outward
