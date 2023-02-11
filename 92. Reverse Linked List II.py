# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        ans=lst[left-1:right]
        ans=ans[::-1]
        lst=lst[:left-1]+ans+lst[right:]
        ans=ListNode(0)
        tmp=ans
        for i in lst:
            tmp.next=ListNode(i)
            tmp=tmp.next
        return ans.next
                
