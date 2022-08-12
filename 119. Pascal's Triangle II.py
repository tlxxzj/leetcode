class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex+1):
            row2 = [1] *(i + 1)
            for j in range(i-1):
                row2[j+1] = row[j] + row[j+1]
            row = row2
        return row