class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        letters = [
            0,0,
            'abc',
            'def',
            'ghi',
            'jkl',
            'mno',
            'pqrs',
            'tuv',
            'wxyz'
        ]
        ret = ['']
        for digit in digits:
            ret2 = []
            for letter in letters[int(digit)]:
                for s in ret:
                    ret2.append(s+letter)
            ret = ret2
        return ret