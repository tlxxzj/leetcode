class Solution {
public:
    string toHex(unsigned int num) {
        static const char hex[] = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"};
        if (num == 0) return "0";
        string ret = "";
        for(; num; ret=hex[num&15] + ret, num = num >> 4);
        return ret;
    }
};