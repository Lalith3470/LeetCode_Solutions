class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in zip(*board):
            c=0
            val=Counter(i)
            for j in board:
                ans=Counter(j)
                if i[c]!="." and int(val[i[c]])!=int(ans[i[c]]):
                    return False
                c+=1
        c=0
        for i in range(0,9,3):
            e=3
            for j in range(0,9,3):
                s=[]
                s+=board[i][j:e]
                for k in range(i+1,i+3):
                    s+=board[k][j:e]
                s=[val for val in s if val !="."]
                if len(set(s))!=len(s):return False
                e+=3
        return True
