class Solution {
public:
    bool isSafe(int row,int col, int n,vector<string>grid){
        int i=row,j=col;
        while(row>=0 && col>=0){
            if(grid[row][col]=='Q') return false;
            col--;row--;
        }
        row=i;col=j;
        while(col>=0){
            if(grid[row][col]=='Q') return false;
            col--;
        }
        row=i;col=j;
        while(row<n && col>=0){
            if(grid[row][col]=='Q') return false;
            row++;col--;
        }
        return true;
    }
public:
    void solve(int col, int n, vector<string>&grid,vector<vector<string>>&lst){
        if(col==n){
            lst.push_back(grid);
            return;
        }
        for(int row=0;row<n;row++){
            if(isSafe(row,col,n,grid)){
                grid[row][col]='Q';
                solve(col+1,n,grid,lst);
                grid[row][col]='.';
            }
        }
    }
public:
    vector<vector<string>> solveNQueens(int n) {
        string s(n,'.');
        vector<vector<string>>lst;
        vector<string>grid(n);
        for(int i=0; i<n; i++) grid[i]=s;
        solve(0,n,grid,lst);
        return lst;
    }
};
