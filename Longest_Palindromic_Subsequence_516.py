class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """ 区间 DP 题 / 画table 法
        similar to https://leetcode-cn.com/problems/longest-palindromic-subsequence/solution/dai-ma-sui-xiang-lu-dai-ni-xue-tou-dpzi-dv83q/
        或者：
        ccnuacmhdu comment： 其实就是求ｓ和ｓ的逆序的最长公共子序列的。转化成最长公共子序列问题就迎刃而解了。
        DIDIDUDIDI 的comment：https://leetcode-cn.com/problems/longest-palindromic-subsequence/solution/gong-shui-san-xie-qu-jian-dp-qiu-jie-zui-h2ya/
        https://zhuanlan.zhihu.com/p/68409952
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for j in range(n):
            for i in range(j, -1, -1):
                if i == j:
                    dp[i][j] = 1
                elif i == j - 1 and s[i] == s[j]:
                    dp[i][j] = 2
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        # print(dp)
        return dp[0][n - 1]

