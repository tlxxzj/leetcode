class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = {}
        for word in dictionary:
            node = root
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["root"] = True
        
        def getRoot(word):
            chars = []
            node = root
            for c in word:
                if "root" in node:
                    break
                if c not in node:
                    return ""
                node = node[c]
                chars.append(c)
            if "root" in node:
                return "".join(chars)
            return ""
        
        res = []
        for word in sentence.split(" "):
            r = getRoot(word)
            print(word, r)
            if r == "":
                res.append(word)
            else:
                res.append(r)
        
        return " ".join(res)
