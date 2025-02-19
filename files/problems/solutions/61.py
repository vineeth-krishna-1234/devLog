# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # no head or no rotations
        if not head or not k:
            return head

        list_len = 0
        cursor_ = head

        # get the length of the list
        while cursor_:
            list_len += 1
            cursor_ = cursor_.next

        # get the actual number of rotations
        counter = k % list_len

        # if no roatations return
        if not counter:
            return head

        # normal algo used in finding the last nth node
        slow_index = fast_index = head
        while fast_index and fast_index.next:
            if counter:
                counter -= 1
            else:
                slow_index = slow_index.next
            fast_index = fast_index.next

        # head will be the slow's next
        # current slow nodes next should be none as it will be the last
        # fast will be in the end of the linked list which should be attached to the head
        return_head = slow_index.next
        slow_index.next = None
        fast_index.next = head
        return return_head
