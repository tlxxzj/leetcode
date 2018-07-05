class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        n = len(hand)
        if n % W != 0: return False

        cards = {}
        for h in hand:
            cards[h] = cards.get(h, 0) + 1

        hand = list(set(hand))
        hand.sort()
        for h in hand:
            c = cards[h]
            if c == 0: continue
            for i in range(h, h + W):
                x = cards.get(i, 0)
                if x < c:
                    return False
                cards[i] = x - c
        return sum(cards.values()) == 0


