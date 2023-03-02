class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """ greedy 贪心 https://programmercarl.com/0714.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BA%E5%90%AB%E6%89%8B%E7%BB%AD%E8%B4%B9.html#%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95
        这个题其实更适合用 动态规划 greedy 不是太好做
        """
        # 基本思路：最低价买 最高价卖
        max_profits = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if 0 <= prices[i] - min_price <= fee:  # 如果以当前价格卖出亏本，则不卖，继续找下一个可卖点
                # 持有 但不产生利润
                continue
            elif prices[i] - min_price > fee:   # 此时有利润，计算 当前 的利润，同时假买入高价的股票 （min_price = prices[i] - fee），看看是否继续盈利 （如果后面 prices[i] - min_price > fee 那么就继续盈利）
                # 持有 当前 产生的利润
                max_profits += prices[i] - min_price - fee
                # 画出图 只有当 后面的价格 比prices[i] - fee这个价格低 时，卖出手中股票 再买入 新股票才 合算
                # 另外 如果 后面的价格 - min_price > fee, 由于这里 - fee，后面 求 max_profits 时 相当于 + fee 从而把 第一次求  max_profits 减去的fee 补回来了
                min_price = prices[i] - fee
            elif prices[i] < min_price: # 此时有更低的价格，可以买入
                # 买入 （同时 如果有的话 手中股票已经卖出）
                min_price = prices[i]
        return max_profits
