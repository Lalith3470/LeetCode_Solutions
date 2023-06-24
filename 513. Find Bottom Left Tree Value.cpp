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
    int findBottomLeftValue(TreeNode* root) {
        vector<int>lst;
        int cnt=0;
        list<TreeNode *>q;
        q.push_back(root);
        while(!q.empty()){
            vector<int>l;
            int ln=q.size();
            for(int i=0;i<ln;i++){
                TreeNode *tmp=q.front();
                q.pop_front();
                if(tmp){
                    l.push_back(tmp->val);
                    q.push_back(tmp->left);
                    q.push_back(tmp->right);
                }
            }
            if(!l.empty()){
                int val=l.front();
                lst.push_back(val);
                cnt++;
            }
        }
        return lst[cnt-1];
    }
};
