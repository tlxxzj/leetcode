from random import random
from math import sqrt

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        while True:
            x, y = [random()*self.radius*2 + self.x - self.radius, random()*self.radius*2 + self.y - self.radius]
            if sqrt((x-self.x) * (x-self.x) + (y-self.y)*(y-self.y)) <= self.radius:
                return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()