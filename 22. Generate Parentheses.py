class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def generate(left, right, s):
            if left == 0 and right == 0:
                ans.append(s)
                return
            if left > 0:
                generate(left-1, right, s+"(")
            if right > left:
                generate(left, right-1, s+")")
        
        generate(n, n, "")
        return ans