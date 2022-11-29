class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [strs]
        l=[]
        for i in strs:
            l.append(sorted(i))
        final_list=[]
        a=[]
        for i in l:
            if i not in a:
                a.append(i)
        for i in range(len(a)):
            s=[]
            for j in range(i,len(l)):
                if a[i]==l[j]:
                    s.append(strs[j])
            final_list.append(s)
        return final_list
