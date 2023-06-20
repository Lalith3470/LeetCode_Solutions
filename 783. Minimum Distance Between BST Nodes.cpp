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
    int minDiffInBST(TreeNode* root) {
        vector<int>lst;
        list<TreeNode *>q;
        q.push_back(root);
        while(!q.empty()){
            int ln=q.size();
            for(int i=0;i<ln;i++){
                TreeNode * tmp=q.front();
                q.pop_front();
                if(tmp){
                    lst.push_back(tmp->val);
                    q.push_back(tmp->left);
                    q.push_back(tmp->right);
                }
            }
        }
        sort(lst.begin(),lst.end());
        int mn=INT_MAX;
        for(int i=0;i<lst.size()-1;i++){
            mn=min(abs(lst[i]-lst[i+1]),mn);
        }
        return mn;
    }
};
