class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """ 62 题 https://leetcode-cn.com/problems/unique-paths/solution/dong-tai-gui-hua-by-powcai-2/ 的变体
        https://leetcode-cn.com/problems/unique-paths-ii/solution/bu-tong-lu-jing-ii-by-leetcode-solution-2/ 视频
        时间复杂度：O(nm)
        空间复杂度：O(m)

        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        curr = [1] * n
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    curr[j] = 0
                # 注意第一行和第一列中也可能有障碍
                elif i == 0:
                    # 上边界：右一个值只和前一个值一样
                    curr[j] = curr[j - 1]
                elif j == 0:
                    # 左边界：下一个值只与上一个值一样
                    # omitted curr[j] = curr[j]
                    continue
                else:
                    curr[j] += curr[j - 1]
        return curr[-1]
