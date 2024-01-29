class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        def diff(w1, w2):
            ans = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    ans += 1
                if ans > 1:
                    break
            return ans

        wordList.append(beginWord)
        diff1 = {}
        for w in wordList:
            diff1[w] = []
        n = len(wordList)

        for i in range(n):
            for j in range(1, n):
                w1, w2 = wordList[i], wordList[j]
                if diff(w1, w2) == 1:
                    diff1[w1].append(w2)
                    diff1[w2].append(w1)
        
        found = False
        prev = {endWord: endWord}
        q = [endWord]
        while len(q) > 0 and (not found):
            q2 = []
            prev2 = {}
            
            for w1 in q:
                for w2 in diff1[w1]:
                    if w2 == beginWord:
                        found = True
                    if w2 not in prev2:
                        prev2[w2] = set([w1])
                    else:
                        prev2[w2].add(w1)
            
            for w in prev2:
                if w not in prev:
                    prev[w] = prev2[w]
                    q2.append(w)
            q = q2
        
        if not found:
            return []


        end = False
        ans = [[beginWord]]
        while not end:
            ans2 = []
            for seq in ans:
                lastw = seq[-1]
                nextw = prev[lastw]
                if lastw != nextw:
                    for w in nextw:
                        ans2.append(seq+[w])
                else:
                    end = True
            if not end:
                ans = ans2
        return ans

                    


