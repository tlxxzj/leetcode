class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append((timestamp, value))
        else:
            self.d[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        i = bisect.bisect_right(self.d[key], (timestamp, chr(127)))
        if i > 0:
            return self.d[key][i-1][1]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)