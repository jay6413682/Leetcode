class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ DP / 股票问题 / 背包问题？https://leetcode-cn.com/circle/article/qiAgHn/ 
        stormsunshine @唐泽 只有在买入的时候才更新交易次数，卖出的时候不更新交易次数。
        """
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        """ 贪心 https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/tan-xin-suan-fa-by-liweiwei1419-2/
        求 单增区间和
        """
        max_profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                max_profit += (prices[i + 1] - prices[i])
        return max_profit
