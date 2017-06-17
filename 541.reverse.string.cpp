class Solution {
public:
    string reverseStr(string s, int k) {
        for(int i=0;i*k < s.length(); i+=2) reverse(s.begin()+k*i, min(s.begin()+k*i+k, s.end()) );
        return s;
    }
};