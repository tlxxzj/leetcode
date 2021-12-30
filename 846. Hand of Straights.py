class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        from collections import defaultdict
        n = len(hand)
        if n % groupSize != 0:
            return False
        
        count = defaultdict(int)
        for num in hand:
            count[num] += 1
        
        hand.sort()
        for num in hand:
            if count[num] == 0:
                continue
            for i in range(num, num+groupSize):
                if count[i] == 0:
                    return False
                count[i] -= 1
        
        return True

        
