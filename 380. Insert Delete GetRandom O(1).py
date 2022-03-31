class RandomizedSet:

    def __init__(self):
        self.items = []
        self.set = {}
        self.unused = []

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        if len(self.unused) > 0:
            i = self.unused.pop()
            self.set[val] = i
            self.items[i] = val
        else:
            i = len(self.items)
            self.set[val] = i
            self.items.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val in self.set:
            i = self.set[val]
            del self.set[val]
            self.unused.append(i)
            self.items[i] = None
            if len(self.unused) * 4 > len(self.items):
                self.items = list(filter(lambda x: x!=None, self.items))
                self.unused = []
                self.set = {}
                for i in range(len(self.items)):
                    self.set[self.items[i]] = i
            return True
        return False
    
    def getRandom(self) -> int:
        import random
        while True:
            x = random.choice(self.items)
            if x != None:
                return x


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()