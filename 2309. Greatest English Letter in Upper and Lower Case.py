class Solution:
    def greatestLetter(self, s: str) -> str:
        lst=[]
        for i in s:
            if i.islower():
                if i.upper() in s:
                    lst.append(i.upper())
        lst.sort()
        if len(lst)<1:return ""
        else:return lst[-1]
