class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [int(i) for i in list(str(num))]
        sorted_digits = sorted(digits, reverse=True)
        n = len(digits)
        for i in range(n):
            if digits[i] == sorted_digits[i]:
                continue
            for j in range(n-1, i, -1):
                if digits[j] == sorted_digits[i]:
                    digits[i], digits[j] = digits[j], digits[i]
                    break
            break
        return int(''.join([str(i) for i in digits]))