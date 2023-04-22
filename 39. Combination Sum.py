class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combsums(idx,lst,n,arr,target,final):
            if idx>n:
                if target==0:
                    final.append(lst[:])
                return

            lst.append(arr[idx])

            if arr[idx]<=target:
                
                combsums(idx,lst,n,arr,target-arr[idx],final)
            lst.pop()
            combsums(idx+1,lst,n,arr,target,final)
            
        lst=[]
        n=len(candidates)-1
        final=[]
        combsums(0,lst,n,candidates,target,final)
        return final
