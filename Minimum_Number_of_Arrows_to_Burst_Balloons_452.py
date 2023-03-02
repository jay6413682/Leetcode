class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """ greedy 贪心 从左到右 每一箭射最多的气球 https://programmercarl.com/0452.%E7%94%A8%E6%9C%80%E5%B0%91%E6%95%B0%E9%87%8F%E7%9A%84%E7%AE%AD%E5%BC%95%E7%88%86%E6%B0%94%E7%90%83.html#%E6%80%9D%E8%B7%AF
        局部最优：当气球出现重叠，一起射，所用弓箭最少。全局最优：把所有气球射爆所用弓箭最少。
        """
        points.sort(key=lambda x: x[0])
        curr_overlapping_end = points[0][1]
        min_arrow_count = 1 # points 不为空至少需要一支箭
        i = 1
        while i < len(points):
            # 如果当前 气球 start <= 当前重叠区域 的右缘 ， 更新 重叠区域 的右缘 为 当前气球右缘 与 当前重叠区域 的右缘 的较小值
            if points[i][0] <= curr_overlapping_end:
                curr_overlapping_end = min(points[i][1], curr_overlapping_end)
            else:
                # 否则 前面的气球都打掉了，至少还需要一根arrow 来打掉现在的 气球，arrow count + 1
                min_arrow_count += 1
                # 更新 重叠区域 的右缘 为 当前气球的右缘
                curr_overlapping_end = points[i][1]
            i += 1
        return min_arrow_count
