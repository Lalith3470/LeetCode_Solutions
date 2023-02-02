class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        ans=[]
        for i in range(0,len(lst),2):
            val=lst[i:i+2]
            ans+=val[::-1]
        final=ListNode(0)
        tmp=final
        for i in ans:
            tmp.next=ListNode(i)
            tmp=tmp.next
        return final.next
