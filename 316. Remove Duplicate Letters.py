class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        def letter_index(c):
            return ord(c) - ord('a')
        
        letters = [0] * 26
        for c in s:
            letters[letter_index(c)] += 1
        
        s2 = []
        s2_letters = [0] * 26
        for c in s:
            i = letter_index(c)
            if s2_letters[i] == 0:
                while len(s2) > 0 and c < s2[-1]:
                    if letters[letter_index(s2[-1])] > 0:
                        s2_letters[letter_index(s2[-1])] = 0
                        s2.pop()
                    else:
                        break
            
            if s2_letters[i] == 0:
                s2.append(c)
            s2_letters[i] = 1
            letters[i] -= 1
            #print(s2)
        
        return "".join(s2)
