import re
class Solution:
    def validIPAddress(self, IP: str) -> str:
        ip = IP
        if ip.count('.') == 3:
            numbers = ip.split('.')
            for num in numbers:
                if (not num.isdigit()) or \
                    int(num) > 255 or \
                    num != str(int(num)):
                    return 'Neither'
            return 'IPv4'
        elif ip.count(':') == 7:
            numbers = ip.split(':')
            for num in numbers:
                if not re.match('^(([0-9a-f]{1,4})|0)$', num, re.IGNORECASE):
                    return 'Neither'
            return 'IPv6'
        return 'Neither'