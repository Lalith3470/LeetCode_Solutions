# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst=[]
        while head:
            if lst and lst[-1]==head.val:
                head=head.next
            else:
                lst.append(head.val)
        if not lst:
            return
        final_lst=ListNode(lst[0])
        tmp=final_lst
        for i in range(1,len(lst)):
            tmp.next=ListNode(lst[i])
            tmp=tmp.next
        return final_lst
        
