class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt=Counter(s)
        c=0
        for i in cnt.values():
            if i%2!=0:
                c+=1
        if c==0:
            return len(s)
        return len(s)-c+1
