class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        lst1,lst2=[],[]
        for i in s:
            if lst1 and i=="#":
                lst1.pop()
            elif i!="#":
                lst1.append(i)
        for i in t:
            if lst2 and i=="#":
                lst2.pop()
            elif i!="#":
                lst2.append(i)
        return lst1==lst2
