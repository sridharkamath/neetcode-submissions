# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge2Lists(self, list1: List[Optional[ListNode]], list2: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode()
        a,b=list1,list2
        curr=dummy
        while a and b:
            if a.val<b.val:
                curr.next=a
                a=a.next
            else:
                curr.next=b
                b=b.next
            curr=curr.next
        curr.next= a or b
        return dummy.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        for i in range(1,len(lists)):
            lists[i]=self.merge2Lists(lists[i],lists[i-1])

        return lists[-1]
