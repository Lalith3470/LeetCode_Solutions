class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a==b:
            return -1
        elif len(a)!=len(b):
            return max(len(a),len(b))
        else:
            return len(a)
