class Codec:

    def __init__(self):
        self._url = {}
        self._url2 = {}
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self._url:
            shortUrl = 'http://tinyurl.com/' + str(len(self._url))
            self._url[longUrl] = shortUrl
            self._url2[shortUrl] = longUrl
        return self._url[longUrl]
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self._url2[shortUrl]
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))