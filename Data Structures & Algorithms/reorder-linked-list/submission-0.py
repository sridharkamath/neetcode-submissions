# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s=f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        m=s
        prev=None
        curr=m
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        curr=head
        last=prev
        while curr!=m:
            nxt=curr.next
            curr.next=last
            last=last.next
            if not last:
                break
            curr.next.next=nxt
            curr=nxt
        

        
            
             
        