class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper() or word.islower():
            return True
        if word[0].isupper() and (len(word)==1 or word[1:].islower()):
            return True
        return False