class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        lst=lst[::-1]
        ans=[]
        for i in range(len(lst)):
            if i!=n-1:
                ans.append(lst[i])
        ans=ans[::-1]
        final=ListNode(0)
        tmp=final
        for i in ans:
            tmp.next=ListNode(i)
            tmp=tmp.next
        return final.next
