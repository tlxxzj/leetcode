class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        ret, rl, d1, d2 = [], float('inf'), {}, {}
        for i in range(len(list1)):
            d1[list1[i]] = i
        for i in range(len(list2)):
            d2[list2[i]] = i
        for r in list1:
            if r in d2:
                l = d1[r] + d2[r]
                if l == rl:
                    ret.append(r)
                elif l < rl:
                    rl = l
                    ret = [r]
        return ret

