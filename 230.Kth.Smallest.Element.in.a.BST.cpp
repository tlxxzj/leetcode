/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        auto node = root;
        stack<TreeNode*>st;
        while(1)
        {
            if(node)
            {
                st.push(node);
                node = node->left;
            }
            else if (!st.empty())
            {
                node = st.top(); st.pop();
                k--;
                if(k==0)
                {
                    return node->val;
                }
                node = node->right;
            }
        }
        return 0;
    }
};