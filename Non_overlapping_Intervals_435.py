class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 贪心 ： 其实类似 452: 先求最少多少箭 可以射破所有气球；气球总个数 - 箭数 就是 答案
        # https://programmercarl.com/0435.%E6%97%A0%E9%87%8D%E5%8F%A0%E5%8C%BA%E9%97%B4.html#%E8%A1%A5%E5%85%85-2
        arrow_counts = 1
        intervals.sort(key=lambda x: x[0])
        where_to_shoot = intervals[0][1]
        n = len(intervals)
        for i in range(1, n):
            if intervals[i][0] >= where_to_shoot:
                where_to_shoot = intervals[i][1]
                arrow_counts += 1
            else:
                where_to_shoot = min(where_to_shoot, intervals[i][1])
        return n - arrow_counts
