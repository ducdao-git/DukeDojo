# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:  # runtime O(n), space O(1)
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


# Question URL: https://neetcode.io/problems/reverse-a-linked-list/question?list=blind75
# Solution: ? -- runtime O(n), space O(1)
