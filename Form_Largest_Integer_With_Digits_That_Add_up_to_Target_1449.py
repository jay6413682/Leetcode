class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        """ DP 背包问题 https://leetcode.cn/problems/form-largest-integer-with-digits-that-add-up-to-target/solution/xiang-xi-jiang-jie-wan-quan-bei-bao-zhuang-tai-de-/
        另一种 完全背包 + 贪心的解法：https://mp.weixin.qq.com/s?__biz=MzU4NDE3MTEyMA==&mid=2247488752&idx=1&sn=e7af274d7293558718748d54f7ddade1&chksm=fd9cbfefcaeb36f975c51282ebdcb802bdad81ae7243a027f17471c78d989ddc6caa79546b96&scene=178&cur_album_id=1751702161341628417#rd
        """
        def max_str(str1, str2):
            len1 = len(str1)
            len2 = len(str2)
            if len1 > len2:
                return str1
            if len1 < len2:
                return str2
            return str1 if str1 > str2 else str2
        n = len(cost)
        dp = [[None for _ in range(target + 1)] for _ in range(n + 1)]
        dp[0][0] = ''
        for i in range(1, n + 1):
            for j in range(target + 1):
                # not choose i
                dp[i][j] = dp[i - 1][j]
                if j - cost[i - 1] >= 0 and dp[i][j - cost[i - 1]] is not None:
                    # choose i at least one time
                    if dp[i][j] is not None:
                        dp[i][j] = max_str(dp[i][j], str(i) + dp[i][j - cost[i - 1]])
                    else:
                        dp[i][j] = str(i) + dp[i][j - cost[i - 1]]
        # print(dp)
        return dp[n][target] if dp[n][target] is not None else "0"