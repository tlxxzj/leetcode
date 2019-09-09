class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        ret = []
        dict.sort(key=lambda x: len(x))
        for word in sentence.split(' '):
            r = word
            for root in dict:
                if word.startswith(root):
                    r = root
                    break
            ret.append(r)
        return ' '.join(ret)