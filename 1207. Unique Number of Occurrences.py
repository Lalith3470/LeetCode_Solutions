class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        lst=[]
        count=Counter(arr)
        for i,j in count.items():
            lst.append(j)
        return len(set(lst))==len(lst)
