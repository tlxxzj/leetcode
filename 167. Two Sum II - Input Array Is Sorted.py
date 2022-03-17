class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while True:
            k = numbers[i] + numbers[j]
            if k < target:
                i += 1 
            elif k > target:
                j -= 1
            else:
                return [i+1, j+1]
