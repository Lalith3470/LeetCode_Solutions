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
    void dfs(TreeNode * root,vector<int>&lst){
        if(root->left)dfs(root->left,lst);
        lst.push_back(root->val);
        if(root->right)dfs(root->right,lst);
    }
public:
    bool findTarget(TreeNode* root, int k) {
        vector<int>lst;
        dfs(root,lst);
        int lo=0,hi=lst.size()-1;
        while(lo<hi){
            int sm=lst[lo]+lst[hi];
            if(sm==k)return true;
            else if(sm>k)hi--;
            else lo++;
        }
        return false;
    }
};
