class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        from collections import defaultdict
        ret = defaultdict(int)
        for cpdomain in cpdomains:
            count, cpdomain = cpdomain.split(' ')
            count = int(count)
            dots = cpdomain.split('.')
            for i in range(len(dots)):
                domain = '.'.join(dots[i:])
                ret[domain] += count
        return [f'{count} {domain}' for domain, count in ret.items()]