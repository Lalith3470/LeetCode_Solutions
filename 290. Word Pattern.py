class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        ln=set(zip(pattern, s))
        if len(pattern)!=len(s):
            return False
        return len(ln)==len(set(pattern)) == len(set(s))
