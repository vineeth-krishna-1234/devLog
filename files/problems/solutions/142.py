# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast_cursor = slow_cursor=head

        while fast_cursor and fast_cursor.next:
            fast_cursor = fast_cursor.next.next
            slow_cursor = slow_cursor.next
            if fast_cursor == slow_cursor:
                break
        else:
            return None
        
        fast_cursor = head
        while fast_cursor != slow_cursor:
            fast_cursor=fast_cursor.next
            slow_cursor=slow_cursor.next
        
        return fast_cursor

