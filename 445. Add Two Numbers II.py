class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=""
        s2=""
        while l1:
            s1+=str(l1.val)
            l1=l1.next
        while l2:
            s2+=str(l2.val)
            l2=l2.next
        ans=str(int(s1)+int(s2))
        final=ListNode(0)
        tmp=final
        for i in ans:
            tmp.next=ListNode(int(i))
            tmp=tmp.next
        return final.next
