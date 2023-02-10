# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        tmp,tmp1=[],[]
        for i in lst:
            if i<x:
                tmp.append(i)
            else:
                tmp1.append(i)
        tmp+=tmp1
        final_lst=ListNode(0)
        val=final_lst
        for i in tmp:
            val.next=ListNode(i)
            val=val.next
        return final_lst.next
