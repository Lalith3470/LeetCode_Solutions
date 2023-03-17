class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cnt=Counter(s)
        lst=[]
        c=0
        tmp=set()
        st=""
        for i in s:
            if i not in tmp:
                tmp.add(i)
                st+=i
                c+=1
            else:st+=i
            cnt[i]-=1
            if cnt[i]==0:
                c-=1
            if c==0:
                lst.append(len(st))
                st=""
        return lst   
