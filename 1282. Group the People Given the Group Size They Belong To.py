class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        ids={}
        for i in range(len(groupSizes)):
            if groupSizes[i] in ids:
                ids[groupSizes[i]]+=[i]
            else:
                ids[groupSizes[i]]=[i]
        lst=[]
        for i,j in sorted(ids.items(), key=lambda val: val[0]):
            if i!=len(j):
                for val in range(0,len(j),i):
                    lst.append(j[val:val+i])
            else:lst.append(j)
        return lst
