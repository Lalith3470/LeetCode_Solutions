class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        k=[]
        l=[]
        for i in range(len(arr)-1):
            sum=abs(arr[i]-arr[i+1])
            l.append(sum)
            k.append([arr[i],arr[i+1]])
        s=min(l)
        l2=[]
        for i in range(len(l)):
            if l[i]==s:
                l2.append(k[i])
        return l2
