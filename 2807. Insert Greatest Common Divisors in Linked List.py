# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        dp=[lst[0]]
        for i in range(1,len(lst)):
            dp.append(gcd(dp[-1],lst[i]))
            dp.append(lst[i])
        a=ListNode(0)
        tmp=a
        for i in dp:
            tmp.next=ListNode(i)
            tmp=tmp.next
        return a.next
