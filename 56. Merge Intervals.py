class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        from functools import cmp_to_key
        def interval_cmp(a, b):
            if a[0] < b[0]:
                return -1
            elif a[0] == b[0]:
                if a[1] < b[1]:
                    return -1
                elif a[1] == b[1]:
                    return 0
                else:
                    return 1
            else:
                return 1
        
        intervals.sort(key=cmp_to_key(interval_cmp))
        merged_intervals = []
        last_interval = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= last_interval[1]:
                last_interval = [last_interval[0], max(last_interval[1], interval[1])]
                continue
            else:
                merged_intervals.append(last_interval)
                last_interval = interval
        merged_intervals.append(last_interval)
        return merged_intervals
