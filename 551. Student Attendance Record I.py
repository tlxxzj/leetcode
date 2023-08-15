class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0
        for r in s:
            if r == 'A':
                late = 0
                absent += 1
                if absent >= 2:
                    return False
            elif r == 'L':
                late += 1
                if late >= 3:
                    return False
            else:
                late = 0
        return True
