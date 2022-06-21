class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """ dp path 路径问题：https://mp.weixin.qq.com/s?__biz=MzU4NDE3MTEyMA==&mid=2247485163&idx=1&sn=ffe456777bcda52c036e6eb2181d1932&chksm=fd9cadf4caeb24e21a57ce47295a54ee9d591dfbb857549a57c145cdeeabf8c4324b007fc18b&token=1459317048&lang=zh_CN&scene=21#wechat_redirect """
        n = len(matrix)
        dp = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == 0:
                    dp[i][j] = matrix[i][j]
                elif j == 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
                elif j == n - 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j + 1]) + matrix[i][j]
        return min(dp[-1])
