class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        lst=[]
        for i in image:
            temp=[]
            for j in i:
                if j==1:
                    temp.append(0)
                else:
                    temp.append(1)
            lst.append(temp[::-1])
        return lst

    
