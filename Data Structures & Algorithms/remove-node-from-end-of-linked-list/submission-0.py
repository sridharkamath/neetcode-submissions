# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        curr=head
        while curr:
            l+=1
            curr=curr.next
        if n==l:
            curr=head
            head=curr.next
            curr.next=None
        else:
            curr=head
            for i in range(l-n-1):
                curr=curr.next
            nxt=curr.next
            curr.next=nxt.next
            nxt.next=None
        return head
            