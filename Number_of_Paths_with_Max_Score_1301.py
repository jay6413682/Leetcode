class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        """ my own dp solution. 解题思路可看https://mp.weixin.qq.com/s?__biz=MzU4NDE3MTEyMA==&mid=2247485565&idx=1&sn=9d307e3ef239d9ba509624736408fc3c&scene=21#wechat_redirect，她的解就算了。
        注意：每个数字都是正数
        """
        # 从左上到右下等价从右下到左上
        # dp[i][j] 表示走到位置（i，j）最大分值
        # dpp[i][j] 表示走到位置（i，j）的最大分值的路径数。
        n = len(board)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dpp = [[0 for _ in range(n)] for _ in range(n)]
        mod = 10 ** 9 + 7
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'X':
                    # 如果board[i][j] == 'X', 即为障碍最大数和为零，最大数和路径数也是0（到不了）
                    continue
                current_val = 0 if board[i][j] == 'E' or board[i][j] == 'S' else int(board[i][j])
                max_dp = 0
                if i == 0 and j == 0:
                    # 初始路径为1条
                    dpp[i][j] = 1
                    # 初始最大数和为0
                    dp[i][j] = 0
                elif i >= 1 and j >= 1:
                    max_dp = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
                    # 不在左边界上边界，且左上不是初始，若左，上，左上都是0（到不了），i，j也到不了（为0）
                    if max_dp == 0 and not (i == 1 and j == 1):
                        continue
                    for x, y in [(i - 1, j - 1), (i - 1, j), (i, j - 1)]:
                        if dp[x][y] == max_dp:
                            dpp[i][j] += dpp[x][y]
                elif i == 0 and j >= 1:
                    # 上边界，且左侧不为初始，若左侧为0（到不了），i，j也到不了（为0）
                    if dp[i][j - 1] == 0 and not (i == 0 and j == 1):
                        continue
                    max_dp = dp[i][j - 1]
                    dpp[i][j] += dpp[i][j - 1]
                elif i >= 1 and j == 0:
                    # 左边界，且上方不为初始，若上方为0（到不了），i，j也到不了（为0）
                    if dp[i - 1][j] == 0 and not (i == 1 and j == 0):
                        continue
                    max_dp = dp[i - 1][j]
                    dpp[i][j] += dpp[i - 1][j]
                dp[i][j] = (max_dp + current_val) % mod
                dpp[i][j] %= mod
        # print(dp, dpp)
        return [dp[n - 1][n - 1], dpp[n - 1][n - 1]]
