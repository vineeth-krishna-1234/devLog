class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        temp_node = ListNode(0,head)

        hare_cursor = tortoise_cursor = temp_node
        while hare_cursor.next:
            if  n :
                n-=1
            else:
                tortoise_cursor=tortoise_cursor.next
            hare_cursor=hare_cursor.next
        else:
            tortoise_cursor.next=tortoise_cursor.next.next if tortoise_cursor.next else None
        return temp_node.next
            



        