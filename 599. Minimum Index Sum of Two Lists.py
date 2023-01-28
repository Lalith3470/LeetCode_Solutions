class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        lst1=[]
        lst2=[]
        for i in list1:
            c=0
            if i in list2:
                c = list1.index(i)+list2.index(i)
                lst1.append(i)
                lst2.append(c)
        res=[]
        for i in range(len(lst2)):
            if lst2[i]==min(lst2):
                res.append(lst1[i])
        return res
        
