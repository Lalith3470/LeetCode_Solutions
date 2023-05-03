class Solution {
public:
    bool isSafe(int row, int col,vector<string>&grid,int n){
        int i=row,j=col;
        while(row>=0 && col>=0){
            if(grid[row][col]=='Q')return false;
            row--;col--;
        }
        row=i;col=j;
        while(col>=0){
            if(grid[row][col]=='Q')return false;
            col--;
        }
        row=i;col=j;
        while(row<n && col>=0){
            if(grid[row][col]=='Q')return false;
            row++;col--;
        }
        return true;
    }
public:
    void nqueen(int col,int n,vector<string>&grid,int &cnt){
        if(col==n){
            cnt++;
            return;
        }
        for(int row=0;row<n;row++){
            if(isSafe(row,col,grid,n)){
                grid[row][col]='Q';
                nqueen(col+1,n,grid,cnt);
                grid[row][col]='.';
            }
        }
    }
public:
    int totalNQueens(int n) {
        vector<string>grid(n);
        string s(n,'.');
        for(int i=0; i<n; i++)grid[i]=s;
        int cnt=0;
        nqueen(0,n,grid,cnt);
        return cnt;
    }
};
