class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cnt=0
        last=0
        for c in s:
            if c == 'A':
                cnt += 1
                if cnt > 1:
                    return False
        return 'LLL' not in s
        