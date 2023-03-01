class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        s=[]
        for i in range(len(letters)):
            s.append(ord(letters[i]))
        
        s.sort()
        for i in range(len(s)):
            if ord(target)<s[i]:
                return chr(s[i])
        return chr(s[0])
