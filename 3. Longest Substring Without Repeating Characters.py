class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt=0
        st=""
        i=0
        while i<len(s):
            if s[i] not in st:
                st +=s[i]
                cnt=max(cnt,len(st))
                i+=1
            else:
                st=st[1:]

        return cnt
