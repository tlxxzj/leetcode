class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num<10:
            return num
        digits = []
        while num>0:
            digits.append(num%10)
            num/=10
        
        digits.reverse()
        #print digits
        n = len(digits)
        for i in xrange(n):
            k=-1
            for j in xrange(n-1,i,-1):
                if k==-1 or digits[j]>digits[k]:
                    k=j
            if k>0 and digits[k]>digits[i]:
                digits[k], digits[i] = digits[i], digits[k]
                return reduce(lambda x,y: x*10+y, digits, 0)
        return reduce(lambda x, y: x*10+y, digits, 0)