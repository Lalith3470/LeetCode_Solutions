/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int dfs(TreeNode* root,int &sm,vector<int>tmp){
        if(root==NULL) return 0;
        tmp.push_back(root->val);
        if(root->left==NULL && root->right==NULL){
            string s;
            for(auto i:tmp) s+=to_string(i);
            sm+=stoi(s);
        }
        dfs(root->left,sm,tmp);
        dfs(root->right,sm,tmp);
        return sm;
    }
public:
    int sumNumbers(TreeNode* root) {
        int sm=0;
        vector<int>tmp;
        return dfs(root,sm,tmp);
    }
};
