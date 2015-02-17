class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """ dp / common sub string problem / 画表解决
        https://zhuanlan.zhihu.com/p/68409952
        https://leetcode.com/discuss/general-discussion/458695/Dynamic-Programming-Patterns#Minimum-(Maximum)-Path-to-Reach-a-Target 
        """
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]