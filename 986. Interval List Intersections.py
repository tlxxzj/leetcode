class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        i, j = 0, 0
        lena, lenb = len(A), len(B)
        while i < lena and j < lenb:
            if A[i][0] > B[j][1]:
                j += 1
                continue
            if A[i][1] < B[j][0]:
                i += 1
                continue
            if B[j][0] <= A[i][0] <= A[i][1] <= B[j][1]:
                x = [A[i][0], A[i][1]]
            elif A[i][0] <= B[j][0] <= B[j][1] <= A[i][1]:
                x = [B[j][0], B[j][1]]
            elif B[j][0] <= A[i][0] <= B[j][1]:
                x = [A[i][0], B[j][1]]
            elif B[j][0] <= A[i][1] <= B[j][1]:
                x = [B[j][0], A[i][1]]
            
            ret.append(x)
            if A[i][1] < B[j][1]:
                i += 1
            elif A[i][1] > B[j][1]:
                j += 1
            else:
                i += 1
                j += 1            
        
        return ret