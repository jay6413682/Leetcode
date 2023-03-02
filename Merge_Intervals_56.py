class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """ 贪心 greedy 同 763. Partition Labels https://programmercarl.com/0056.%E5%90%88%E5%B9%B6%E5%8C%BA%E9%97%B4.html#%E6%80%9D%E8%B7%AF
        """
        intervals.sort(key=lambda x: x[0])
        curr_merged_interval_start, curr_merged_interval_end = intervals[0][0], intervals[0][1]
        res = []
        for itv in intervals:
            if itv[0] > curr_merged_interval_end:
                res.append([curr_merged_interval_start, curr_merged_interval_end])
                curr_merged_interval_start = itv[0]
            curr_merged_interval_end = max(itv[1], curr_merged_interval_end)
        res.append([curr_merged_interval_start, curr_merged_interval_end])
        return res
