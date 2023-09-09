class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>>lst;
        list<TreeNode* >q;
        q.push_back(root);
        while(q.size()!=0){
            vector<int>l;
            int ln=q.size();
            for(int i=0; i<ln;i++){
                TreeNode* tmp=q.front();
                q.pop_front();
                if(tmp){
                    l.push_back(tmp->val);
                    q.push_back(tmp->left);
                    q.push_back(tmp->right);
                }
            }
            if(!l.empty()) lst.push_back(l);
        }
        return lst;
    }
};
