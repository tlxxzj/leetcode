class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        digits.reverse()
        n = len(digits)
        digits[0] += 1
        i = 0
        while digits[i] > 9:
            digits[i] = digits[i] % 10
            i += 1
            if i == n:
                digits.append(0)
            digits[i] += 1
        digits.reverse()
        return digits
        