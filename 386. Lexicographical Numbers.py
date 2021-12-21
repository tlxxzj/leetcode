class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ret = []
        def getNums(num):
            ret.append(num)
            for i in range(10):
                num2 = num * 10 + i
                if num2 <= n:
                    getNums(num2)
                else:
                    break
        for i in range(1, min(10, n+1)):
            getNums(i)
        
        return ret