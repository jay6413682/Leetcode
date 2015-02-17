class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        """ dynamic programming, dp，类似1130题: https://leetcode-cn.com/problems/minimum-score-triangulation-of-polygon/solution/qu-jian-dong-tai-gui-hua-4ms-by-njyang-yang-yang/ . 注意下面的评论：
        i为什么需要倒序遍历： 比如在计算dp[0][3]时，需要用到dp[0][1]和dp[1][3]（m=1的情况）、dp[0][2]和dp[2][3]（m=2的情况），即需要dp[0][3]左侧和下边的结果先计算好，所以用倒序可以完成这个要求。

        https://zhidao.baidu.com/question/351493947.html: 不会有相交对角线： n边形过一个顶点引出所有对角线后，把多边形分成n-2个三角形
        """
        n = len(values)
        dp = [[float(inf) for _ in range(n)] for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                # print(i, j)
                if i + 1 == j:
                    dp[i][j] = 0
                    # print(i, j, n, dp)
                elif i + 2 == j:
                    dp[i][j] = values[i] * values[i + 1] * values[j]
                    # print(i, j, n, dp)
                else:
                    for m in range(i + 1, j):
                        # print(i, m, j, n, dp)
                        dp[i][j] = min(dp[i][j], dp[i][m] + values[i] * values[m] * values[j] + dp[m][j])
        return dp[0][n - 1]
