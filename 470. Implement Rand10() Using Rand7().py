# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            x = (rand7()-1) * 7 + (rand7()-1) + 1
            if x <= 10:
                return x
