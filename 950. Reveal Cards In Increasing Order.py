class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        from collections import deque
        de = deque([])
        deck.sort(reverse=True)
        for i in deck:
            if len(de) > 1:
                r = de.pop()
                de.appendleft(r)
            de.appendleft(i)
        return list(de)