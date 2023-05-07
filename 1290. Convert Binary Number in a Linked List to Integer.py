class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        s=""
        while head:
            s+=str(head.val)
            head=head.next
        return int(s,2)
