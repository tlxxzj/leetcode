class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        i2r = {
            1:'I',
            5:'V',
            10:'X',
            50:'L',
            100:'C',
            500:'D',
            1000:'M'
        }
        l10 = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        ret = ''
        while num >= 1000:
            ret += i2r[1000]
            num -= 1000
        while num >= 500:
            if num >= 900:
                ret += 'CM'
                num -=900
                continue
            ret += i2r[500]
            num -= 500
        while num >= 100:
            if num >= 400:
                ret += 'CD'
                num -= 400
                continue
            ret += i2r[100]
            num -= 100
        while num >= 50:
            if num >= 90:
                ret += 'XC'
                num -= 90
                continue
            ret += i2r[50]
            num -= 50
        while num >= 10:
            if num >= 40:
                ret += 'XL'
                num -= 40
                continue
            ret += i2r[10]
            num -= 10
        ret += l10[num]
        return ret
        