class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        a = ''
        for i in range(len(s)):
            if s[i].isalnum():
                a+=s[i].lower()
        
        return len(a)<1 or a==a[::-1]
