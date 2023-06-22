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
    void dfs(TreeNode *root,int val){
        if(root->val>val){
            if(root->left==NULL) root->left=new TreeNode(val);
            else dfs(root->left,val);
        }
        if(root->val<val){
            if(root->right==NULL) root->right=new TreeNode(val);
            else dfs(root->right,val);
        }
    }
public:
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        TreeNode *node=new TreeNode(preorder[0]);
        for(int i=1; i<preorder.size(); i++) dfs(node,preorder[i]);
        return node;
    }
};
