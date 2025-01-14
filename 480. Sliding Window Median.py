class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        from heapq import heappush, heappop
        class Heap:
            def __init__(self, k):
                self.k = k
                self.small = []
                self.large = []
                self.smallLen = 0
                self.largeLen = 0
                self.poped = {}
            
            def push(self, x):
                if len(self.small) == 0 or x <= -self.small[0]:
                    heappush(self.small, -x)
                    self.smallLen += 1
                else:
                    heappush(self.large, x)
                    self.largeLen += 1
                self.balance()
            
            def pop(self, x):
                self.poped[x] = self.poped.get(x, 0) + 1
                if x <= -self.small[0]:
                    self.smallLen -= 1
                else:
                    self.largeLen -= 1
                self.balance()
            
            def prune(self, h):
                while h:
                    x = h[0]
                    if h is self.small:
                        x = -x
                    y = self.poped.get(x, 0)
                    if y > 0:
                        if y == 1:
                            self.poped.pop(x)
                        else:
                            self.poped[x] -= 1
                        heappop(h)
                    else:
                        break
                    
            def balance(self):
                if self.smallLen > self.largeLen + 1:
                    heappush(self.large, -self.small[0])
                    heappop(self.small)
                    self.smallLen -= 1
                    self.largeLen += 1
                elif self.smallLen < self.largeLen:
                    heappush(self.small, -self.large[0])
                    heappop(self.large)
                    self.smallLen += 1
                    self.largeLen -= 1
                self.prune(self.small)
                self.prune(self.large)
            
            def median(self):
                if self.k % 2 == 0:
                    return (-self.small[0] + self.large[0])/2
                else:
                    return -self.small[0]
        
        res = []
        h = Heap(k)
        for i in range(k):
            h.push(nums[i])
        
        res.append(h.median())
        for i in range(k, len(nums)):
            h.push(nums[i])
            h.pop(nums[i-k])
            res.append(h.median())
        
        return res