class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        a = ''
        for i in range(len(s)):
            if s[i].isalnum():
                a+=s[i].lower()
        
        if len(a)<1:
            return True
        if a == a[::-1] :
            return True
        else:
            return False
