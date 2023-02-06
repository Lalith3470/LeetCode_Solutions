# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        if not lst:
            return
        for i in range(int(k%len(lst))):
            lst=[lst[-1]]+lst[:-1]
        ans=ListNode(0)
        tmp=ans
        for i in lst:
            tmp.next=ListNode(i)
            tmp=tmp.next
        return ans.next
