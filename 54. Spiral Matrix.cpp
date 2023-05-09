class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int>lst;
        int n=matrix.size(),m=matrix[0].size();
        int up=0,down=n-1,left=0,right=m-1;
        while(up<=down && left<=right){
            for(int i=left;i<=right;i++) lst.push_back(matrix[up][i]);
            up++;
            for(int i=up;i<=down;i++) lst.push_back(matrix[i][right]);
            right--;
            if(up<=down){
                for(int i=right;i>=left;i--) lst.push_back(matrix[down][i]);
                down--;
            }
            if(left<=right){
            for(int i=down;i>=up;i--) lst.push_back(matrix[i][left]);
            left++;
            }
        }
        return lst;
    }
};
