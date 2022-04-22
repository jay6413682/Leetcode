class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ dp/股票问题/类似多维背包问题？: https://leetcode-cn.com/circle/article/qiAgHn/ 
        stormsunshine @唐泽 只有在买入的时候才更新交易次数，卖出的时候不更新交易次数。
        """
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        return dp[n - 1][0]
