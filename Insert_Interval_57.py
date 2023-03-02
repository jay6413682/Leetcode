class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # greedy 贪心 同 56. Merge Intervals
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        res = []
        curr_non_overlap_start, curr_non_overlap_end = intervals[0]
        for interval in intervals:
            if interval[0] > curr_non_overlap_end:
                res.append([curr_non_overlap_start, curr_non_overlap_end])
                curr_non_overlap_start = interval[0]
            curr_non_overlap_end = max(curr_non_overlap_end, interval[1])
        res.append([curr_non_overlap_start, curr_non_overlap_end])
        return res

        # 思路类似 https://mp.weixin.qq.com/s/ioUlNa4ZToCrun3qb4y4Ow
        res = []
        if not intervals:
            return [newInterval]
        i = 0
        n = len(intervals)
        while i < n:
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            else:
                break
            i += 1
        curr_interval_start, curr_interval_end = newInterval
        while i < n:
            if intervals[i][0] <= newInterval[1]:
                curr_interval_start, curr_interval_end = min(intervals[i][0], curr_interval_start), max(intervals[i][1], curr_interval_end)
            else:
                break
            i += 1
        res.append([curr_interval_start, curr_interval_end])
        while i < n:
            if intervals[i][0] > newInterval[1]:
                res.append(intervals[i])
            else:
                break
            i += 1
        return res

        
        
