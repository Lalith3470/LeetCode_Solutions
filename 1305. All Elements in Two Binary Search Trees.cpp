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
    void dfs(TreeNode* node,vector<int>&lst){
        if(node->left) dfs(node->left,lst);
        lst.push_back(node->val);
        if(node->right) dfs(node->right,lst);
    }
public:
    void dfsc(TreeNode* node,vector<int>&lst){
        if(node->left) dfs(node->left,lst);
        lst.push_back(node->val);
        if(node->right) dfs(node->right,lst);
    }
public:
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        vector<int>lst;
        if(root1)dfs(root1,lst);
        if(root2)dfsc(root2,lst);
        sort(lst.begin(), lst.end());
        return lst;
    }
};
