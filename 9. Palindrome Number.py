class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        if x %10 == 0:
            return False
        
        y = 0
        while x > 0:
            z = x % 10
            x = x // 10
            if x > 0 and x == y:
                return True
            y = y * 10 + z
            if x == y:
                return True
        return False
        