class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        import re
        
        def isV4():
            v4 = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
            if not re.match(v4, queryIP):
                return False
            
            groups = queryIP.split(".")
            
            for group in groups:
                if group[0] == "0" and len(group) > 1:
                    return False
                if int(group) > 255:
                    return False
            return True
            
        
        def isV6():
            v6 = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
            return re.match(v6, queryIP) != None
        
        if isV4():
            return "IPv4"
        elif isV6():
            return "IPv6"
        return "Neither"