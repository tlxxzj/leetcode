class Solution {
public:
    int nextGreaterElement(int n) {
        auto s = to_string(n);
        if (next_permutation(s.begin(), s.end()))
        {
            long x = atol(s.c_str());
            if (x > 0x7fffffff) return -1;
            else return x;
        }
        else return -1;
    }
};