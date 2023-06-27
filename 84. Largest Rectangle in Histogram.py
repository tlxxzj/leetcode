class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [0] * n
        right = [0] * n
        stack = []
        for i in range(n):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) > 0:
                left[i] = stack[-1]+1
            else:
                left[i] = 0
            stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) > 0:
                right[i] = stack[-1]-1
            else:
                right[i] = n-1
            stack.append(i)
        
        res = 0
        for i in range(n):
            res = max(res, (right[i]-left[i]+1) * heights[i])
        
        return res