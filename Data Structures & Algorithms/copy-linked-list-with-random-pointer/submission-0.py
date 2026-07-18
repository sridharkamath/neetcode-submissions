"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        dummy=Node(0,None,None)
        new_curr=dummy
        curr=head
        hm={}

        while curr:
            new_curr.next=Node(curr.val,None,None)
            new_curr=new_curr.next
            hm[curr]=new_curr
            curr=curr.next
            
        curr=head
        new_curr=dummy.next

        while curr:
            if curr.random:
                new_curr.random = hm[curr.random]
            else:
                new_curr.random = None
            new_curr=new_curr.next
            curr=curr.next
        return dummy.next