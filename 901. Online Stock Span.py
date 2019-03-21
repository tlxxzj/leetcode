class StockSpanner:

    def __init__(self):
        self.prices = []
        self.k = 1

    def next(self, price: int) -> int:
        self.prices.append(price)
        if len(self.prices) == 1:
            self.k = 1
            return 1
        if price < self.prices[-2]:
            self.k = 1
            return 1
        if price == self.prices[-2]:
            self.k += 1
            return self.k
        if price > self.prices[-2]:
            self.k += 1
            while self.k < len(self.prices) and self.prices[-self.k - 1] <= price:
                self.k += 1
            return self.k



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)