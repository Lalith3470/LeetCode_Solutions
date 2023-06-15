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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        int cnt=0;
        vector<vector<int>>lst;
        list<TreeNode *>q;
        q.push_back(root);
        while(!q.empty()){
            vector<int>l;
            int ln=q.size();
            for(int i=0; i<ln; i++){
                TreeNode * tmp=q.front();
                q.pop_front();
                if(tmp){
                    l.push_back(tmp->val);
                    q.push_back(tmp->left);
                    q.push_back(tmp->right);
                }
            }
            if(!l.empty()){
                if(cnt%2!=0){
                    reverse(l.begin(),l.end());
                    lst.push_back(l);
                }
                else lst.push_back(l);
            }
            cnt++;
        }
        return lst;
    }
};
