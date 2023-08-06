class Solution:
    def finalString(self, s: str) -> str:
        st=""
        for i in s:
            if i=="i":
                st=st[::-1]
            else:st+=i
        return st
