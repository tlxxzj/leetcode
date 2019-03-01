class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = list(filter(lambda x: x%2 != 0, A))
        even = list(filter(lambda x: x%2 == 0, A))
        n = len(A)
        ret = []
        for i in range(n//2):
            ret.append(even.pop())
            ret.append(odd.pop())
        return ret
        