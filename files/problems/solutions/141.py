# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        hare_index = head
        tortoise_index = head

        while hare_index and hare_index.next:
            hare_index = hare_index.next.next
            tortoise_index = tortoise_index.next
            if hare_index == tortoise_index:
                return True
        return False
