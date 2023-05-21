class Solution {
public:
    bool valid(vector<vector<char>>&board,int row,int col, char c){
        for(int k=0; k<9; k++){
            if(board[row][k]==c) return false;
            if(board[k][col]==c) return false;
            if(board[3 * (row/3) + k/3][3 * (col/3) + k%3]==c)return false;
        }
        return true;
    }
public:
    bool solve(vector<vector<char>>& board){
        for(int i=0; i<9; i++){
            for(int j=0; j<9; j++){
                if(board[i][j]=='.'){
                    for(char c='1'; c<='9'; c++){
                        if(valid(board,i,j,c)){
                            board[i][j]=c;
                            if(solve(board)==true) return true;
                            else board[i][j]='.';
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }
public:
    void solveSudoku(vector<vector<char>>& board) {
        solve(board);
    }
};
