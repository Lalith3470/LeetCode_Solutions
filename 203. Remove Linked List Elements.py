# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        l=[i for i in lst if i!=val]
        final_list=ListNode(0)
        tmp=final_list
        for i in l:
            tmp.next=ListNode(i)
            tmp=tmp.next
        return final_list.next
