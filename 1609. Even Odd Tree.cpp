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
    bool isEvenOddTree(TreeNode* root) {
        list<TreeNode *>q;
        long long cnt=0;
        q.push_back(root);
        while(!q.empty()){
            long long e_val=INT_MAX;
            long long o_val=INT_MIN;
            int ln=q.size();
            for(int i=0; i<ln; i++){
                TreeNode * tmp=q.front();
                q.pop_front();
                if(tmp){
                    if(cnt%2==0){
                        if(tmp->val%2!=0 && o_val<tmp->val){
                            o_val=tmp->val;
                        }
                        else return false;
                    }
                    else{
                        if(tmp->val%2==0 && e_val>tmp->val){
                            e_val=tmp->val;
                        }
                        else return false;
                    }
                    q.push_back(tmp->left);
                    q.push_back(tmp->right);
                }
            }
            cnt++;
        }
        return true;
    }
};
