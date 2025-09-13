class Solution:
    def maxFreqSum(self, s: str) -> int:
        from collections import defaultdict, Counter
        vowel_counter = defaultdict(int)
        consonant_counter = defaultdict(int)
        for c in s:
            if c in 'aeiou':
                vowel_counter[c]+=1
            else:
                consonant_counter[c]+=1
        vowel_counter = Counter(vowel_counter)
        consonant_counter = Counter(consonant_counter)
        vowel_f, consonant_f = 0, 0
        if len(vowel_counter) > 0:
            vowel_f = vowel_counter.most_common(1)[0][1]
        if len(consonant_counter) > 0:
            consonant_f = consonant_counter.most_common(1)[0][1]
        return vowel_f + consonant_f
