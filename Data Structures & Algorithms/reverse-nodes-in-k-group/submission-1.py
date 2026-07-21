# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head, tail):
        curr=head
        prev=tail.next
        while curr!=tail:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        tail = head
        head = curr
        curr.next=prev
        return head, tail
        
            
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr=tail=head
        dummy=ListNode()
        prev=dummy
        while curr and tail:

            for i in range(k-1):
                if not tail:
                    return dummy.next
                tail=tail.next

            if not tail:
                return dummy.next

            rev_curr, rev_tail = self.reverseList(curr,tail)

            prev.next=rev_curr
            prev=rev_tail
            curr=rev_tail.next
            tail=curr

        return dummy.next


