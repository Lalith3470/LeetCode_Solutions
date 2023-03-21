class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l,e,o=[],[],[]
        for i in nums:
            if i%2==0:
                e.append(i)
            else:
                o.append(i)
        for i in range(len(e)):
            l.append(e[i])
            l.append(o[i])
        return l
