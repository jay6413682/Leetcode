
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        """ dp 背包问题 （推荐，更具有一般性） https://mp.weixin.qq.com/s?__biz=MzU4NDE3MTEyMA==&mid=2247488103&idx=1&sn=5767d5691b6c87f15ca3182c3742fc79&chksm=fd9cb978caeb306e6cbb0e1da73c4293e9a817749404db73e69d874b3932502bee3eab98d054&scene=178&cur_album_id=1751702161341628417#rd
        将每个任务看作一个「物品」，完成任务所需要的人数看作「成本」，完成任务得到的利润看作「价值」。

        其特殊在于存在一维容量维度需要满足「不低于」，而不是常规的「不超过」。这需要我们对于某些状态作等价变换。
        由于我们没有设计动规数组存储「利润至少为负权」状态，我们需要根据「状态定义」做一个等价替换，将这个「状态」映射到 dp[i][j][0]。这主要是利用所有的任务利润都为“非负数”，所以不可能出现利润为负的情况，这时候「利润至少为某个负数 」的方案数其实是完全等价于「利润至少为 0」的方案数。
        """
        mod = 10 ** 9 + 7
        # dp[i][j][k] 代表考虑前 i 个任务，使用人数不超过 j，产生利益至少 k 的方案数 
        dp = [[[0 for _ in range(minProfit + 1)] for _ in range(n + 1) ] for _ in range(len(group) + 1)]
        for i in range(0, len(group) + 1):
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    # 初始化：当没有任务时，无论有多少人，只有利益至少为 0 时的方案数为 1，其他为 0 
                    if i == 0 and k == 0:
                        dp[0][j][0] = 1
                    elif i > 0:
                        dp[i][j][k] = dp[i - 1][j][k] 
                        if j >= group[i - 1]:
                            # 由于我们没有设计动规数组存储「利润至少为负权」状态，我们需要根据「状态定义」做一个等价替换，将这个「状态」映射到 dp[i][j][0]。这主要是利用所有的任务利润都为“非负数”，所以不可能出现利润为负的情况，这时候「利润至少为某个负数 」的方案数其实是完全等价于「利润至少为 0」的方案数。
                            if k >= profit[i - 1]:
                                dp[i][j][k] += dp[i - 1][j - group[i - 1]][k - profit[i - 1]]
                            else:
                                dp[i][j][k] += dp[i - 1][j - group[i - 1]][0]
                            dp[i][j][k] %= mod
        # print(dp)
        return dp[len(group)][n][minProfit]


class Solution2:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        """ dp 背包问题 作差法 （不推荐，此方式会随着带「至少」限制的维度的增加，带来代码量的增多和复杂度的上升。） https://mp.weixin.qq.com/s?__biz=MzU4NDE3MTEyMA==&mid=2247488103&idx=1&sn=5767d5691b6c87f15ca3182c3742fc79&chksm=fd9cb978caeb306e6cbb0e1da73c4293e9a817749404db73e69d874b3932502bee3eab98d054&scene=178&cur_album_id=1751702161341628417#rd
        基本思路是先不考虑最小利润 minProfit，求得所有只受「人数限制」的方案数 a。然后求得考虑「人数限制」同时，利润低于 minProfit（不超过 minProfit - 1）的所有方案数 b。最后由 a - b 即是答案。
        """
        mod = 10 ** 9 + 7
        # dp[i][j] 代表考虑前 i 个任务，使用人数不超过 j 方案数 
        dp = [[0 for _ in range(n + 1) ] for _ in range(len(group) + 1)]
        for i in range(len(group) + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[0][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j]
                    if j >= group[i - 1]:
                        dp[i][j] += dp[i - 1][j - group[i - 1]]
        # dp2[i][j][k] 代表考虑前 i 个任务，使用人数不超过 j，产生利益<= k 的方案数
        # 产生利益小于等于minProfit - 1 为 <= -1，不存在
        if minProfit == 0:
            return dp[len(group)][n] % mod
        dp2 = [[[0 for _ in range(minProfit)] for _ in range(n + 1)] for _ in range(len(group) + 1)]
        for i in range(len(group) + 1):
            for j in range(n + 1):
                for k in range(minProfit):
                    # 初始化：当没有任务时，方案数为 1
                    if i == 0:
                        dp2[0][j][k] = 1
                    else:
                        dp2[i][j][k] = dp2[i - 1][j][k] 
                        if j >= group[i - 1] and k >= profit[i - 1]:
                            dp2[i][j][k] += dp2[i - 1][j - group[i - 1]][k - profit[i - 1]]
        # 注意不能在前面给dp 和 dp2 取mod，因为有可能dp 变小了，减完变负值
        return (dp[len(group)][n] - dp2[len(group)][n][minProfit - 1]) % mod
                        