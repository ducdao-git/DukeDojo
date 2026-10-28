# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:  # runtime O(n), space O(1)
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1:
            return list2

        if not list2:
            return list1

        if list1.val < list2.val:
            new_list = list1
            list1 = list1.next
        else:
            new_list = list2
            list2 = list2.next
        new_head = new_list

        while list1 and list2:
            if list1.val < list2.val:
                new_list.next = list1
                list1 = list1.next
            else:
                new_list.next = list2
                list2 = list2.next
            new_list = new_list.next

        new_list.next = list1 if list1 else list2
        return new_head


# Question URL: https://neetcode.io/problems/merge-two-sorted-linked-lists/question?list=blind75
# Solution: ? -- runtime O(n), space O(1)
