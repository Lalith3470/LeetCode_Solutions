class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        s=text.split()
        l=[]
        for i in range(len(s)-2):
            if s[i]==first and  s[i+1]==second:
                l.append(s[i+2])
        return l
 
