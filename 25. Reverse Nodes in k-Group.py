# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        final=[]
        for i in range(0,len(lst),k):
            ans=lst[i:i+k]
            if len(ans)==k:
                final+=ans[::-1]
            else:
                final+=ans
        ans=ListNode(0)
        tmp=ans
        for i in final:
            tmp.next=ListNode(i)
            tmp=tmp.next

        return ans.next
