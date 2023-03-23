class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        lst=[]
        popped=popped[::-1]
        for i in pushed:
            lst.append(i)
            while lst and lst[-1]==popped[-1]:
                lst.pop()
                popped.pop()
        return len(lst)==0
        
