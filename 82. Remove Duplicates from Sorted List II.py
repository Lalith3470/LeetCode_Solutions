# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        dic=Counter(lst)
        final=[]
        for i,j in dic.items():
            if j==1:
                final.append(i)
        ans=ListNode(0)
        tmp=ans
        for i in final:
            tmp.next=ListNode(i)
            tmp=tmp.next
        return ans.next
