class Codec:
    def __init__(self):
        self._count = 0
        self._l2surls = {}
        self._s2lurls = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self._l2surls:
            self._count += 1
            surl = f'https://tinyurl.com/${self._count}'
            self._s2lurls[surl] = longUrl
            self._l2surls[longUrl] = surl
        return self._l2surls[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self._s2lurls[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))