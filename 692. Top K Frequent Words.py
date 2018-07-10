import collections
import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        fq = collections.Counter(words)
        h = [(-f, w) for w, f in fq.items()]
        heapq.heapify(h)
        return [heapq.heappop(h)[1] for i in range(k)]