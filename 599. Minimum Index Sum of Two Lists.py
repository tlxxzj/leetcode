class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m1 = {}
        for i in range(len(list1)):
            m1[list1[i]] = i
        
        commnStr, commonSum = [], len(list1) + len(list2)
        for i in range(len(list2)):
            s = list2[i]
            if s in m1:
                j = m1[s]
                if i + j == commonSum:
                    commnStr.append(s)
                elif i + j < commonSum:
                    commonSum = i + j
                    commnStr = [s]
        return commnStr