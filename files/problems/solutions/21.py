# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        cursor_ = None
        return_head = None
        while list1 and list2:
            node_to_add = None

            if list1.val < list2.val:
                node_to_add = list1
                list1 = list1.next
            else:
                node_to_add = list2
                list2 = list2.next

            if return_head:
                cursor_.next = node_to_add
                cursor_ = cursor_.next
            else:
                return_head = cursor_ = node_to_add
        remaining_nodes = None
        if list1:
            remaining_nodes = list1
        if list2:
            remaining_nodes = list2
        if return_head:
            cursor_.next = remaining_nodes
        else:
            return_head = cursor_ = remaining_nodes
        return return_head
