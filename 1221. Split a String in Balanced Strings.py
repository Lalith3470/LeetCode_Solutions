class Solution:
    def balancedStringSplit(self, s: str) -> int:
        R=0
        L=0
        count = 0
        for i in range(len(s)):
            if s[i] == "R":
                R+=1
            else:
                L+=1
            if R==L:
                count+=1
        return count
