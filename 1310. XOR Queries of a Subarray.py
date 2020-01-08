class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(arr)
        for i in range(1, n):
            arr[i] = arr[i] ^ arr[i-1]
        ret = []
        for x, y in queries:
            if x == 0:
                ret.append(arr[y])
            else:
                ret.append(arr[x-1]^arr[y])
        return ret