class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        """ dp 路径问题：https://mp.weixin.qq.com/s?__biz=MzU4NDE3MTEyMA==&mid=2247485187&idx=1&sn=a07f67501aa696a79b1e85bb2860c0b2&chksm=fd9cac1ccaeb250a777f9334c0cd3bb0135dafa0007d6d0bbb5cf38e484773d3539fd776b2ea&token=1459317048&lang=zh_CN&scene=21#wechat_redirect """
        '''
        # 未优化解
        n = len(grid)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == 0:
                    dp[i][j] = grid[i][j]
                else:
                    for k in range(n):
                        if k != j:
                            dp[i][j] = min(dp[i - 1][k] + grid[i][j], dp[i][j])
        return min(dp[-1])
        '''
        # 优化解
        j1 = j2 = float(-inf)
        n = len(grid)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            tj1 = tj2 = float(-inf)
            for j in range(n):
                if i == 0:
                    dp[i][j] = grid[i][j]
                else:
                    if j == j1:
                        dp[i][j] = dp[i - 1][j2] + grid[i][j]
                    else:
                        dp[i][j] = dp[i - 1][j1] + grid[i][j]
                if tj1 < 0 or dp[i][j] < dp[i][tj1]:
                    tj2, tj1 = tj1, j
                elif tj2 < 0 or dp[i][j] < dp[i][tj2]:
                    tj2 = j
            j1 = tj1
            j2 = tj2
            # print(j1, j2, dp)
        return min(dp[-1])
