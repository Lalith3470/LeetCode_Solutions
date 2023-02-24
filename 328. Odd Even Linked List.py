# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd,evn=[],[]
        c=0
        while head:
            if c%2==0:
                evn.append(head.val)
            else:
                odd.append(head.val)
            c+=1
            head=head.next
        a=ListNode(0)
        tmp=a
        for i in (evn+odd):
            tmp.next=ListNode(i)
            tmp=tmp.next
        return a.next
