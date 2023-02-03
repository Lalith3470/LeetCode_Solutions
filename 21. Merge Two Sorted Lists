# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        lst=[]
        while list1:
            lst.append(list1.val)
            list1=list1.next
        while list2:
            lst.append(list2.val)
            list2=list2.next
        lst.sort()
        ans=ListNode(0)
        val=ans
        for i in lst:
            val.next=ListNode(i)
            val=val.next
        return ans.next
