class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        int l = 0, r = n, m,x = 0;
        while (l<=r)
        {
            m = (l+r)/2;
            if (citations.end() - lower_bound(citations.begin(), citations.end(), m) >= m)
            {
                x = m;
                l = m + 1;
            }
            else
            {
                r = m - 1;
            }
        }
        return x;
    }
};