class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        lst,tmp=[],[]
        mn = len(s)
        for i in range(len(s)):
            if s[i] == c: tmp.append(i)
        for i in range(len(s)):
            for j in range(len(tmp)): mn=min(mn,abs(i-tmp[j]))
            lst.append(mn)
            mn = len(s)
        return lst
