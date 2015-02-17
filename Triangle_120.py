class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """ dp 路径问题 path 优化解：推导过程 https://mp.weixin.qq.com/s?__biz=MzU4NDE3MTEyMA==&mid=2247485123&idx=1&sn=8a427e56d472d1517b0983d8cdc5c629&scene=21#wechat_redirect """
        height = len(triangle)
        dp = [None for _ in range(len(triangle[-1]))]
        for i in range(height):
            for j in range(i, -1, -1):
                if i == 0:
                    dp[j] = triangle[i][j]
                elif j == 0:
                    dp[j] = dp[j] + triangle[i][j]
                elif j == i:
                    dp[j] = dp[j - 1] + triangle[i][j]
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + triangle[i][j]
            # print(dp)
        return min(dp)
