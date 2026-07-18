# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a,b=l1,l2
        carry=0
        dummy=ListNode()
        curr=dummy
        while a and b:
            res=a.val+b.val+carry
            curr.next=ListNode(res%10)
            if res-10>=0:
                carry=1
            else:
                carry=0
            a=a.next
            b=b.next
            curr=curr.next
        while a:
            res=a.val+carry
            curr.next=ListNode(res%10)
            if res-10>=0:
                carry=1
            else:
                carry=0
            curr=curr.next
            a=a.next
        while b:
            res=b.val+carry
            curr.next=ListNode(res%10)
            if res-10>=0:
                carry=1
            else:
                carry=0
            curr=curr.next
            b=b.next
        if carry:
            curr.next=ListNode(1)
        return dummy.next