class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        p={j:i for i,j in enumerate(string. ascii_lowercase,1)}
        sm=sum(shifts)
        stng=""
        for i in range(len(s)):
            temp=(p[s[i]]+sm)/26
            if int(temp)==temp:
                temp=26
            else:
                temp=abs(floor(temp)-temp)*26
                temp=float("%.2f"%temp)
            for ch,val in p.items():
                if val==temp:
                    stng+=ch
            sm-=shifts[i]
        return stng
