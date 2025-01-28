# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        

        str_ =[]
        cursor_ =head

        while cursor_:
            str_.append(cursor_.val)
            cursor_=cursor_.next
        return str_==str_[::-1]