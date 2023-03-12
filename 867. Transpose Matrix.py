class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        lst=[]
        for i in zip(*matrix):
            lst.append(i)
        return lst
