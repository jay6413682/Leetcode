class Solution:
    def numTrees(self, n: int) -> int:
        """ DP My solution based on https://leetcode.com/discuss/general-discussion/458695/Dynamic-Programming-Patterns#Minimum-(Maximum)-Path-to-Reach-a-Target
        not efficient
        """
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        # print(dp)
        for j in range(n):
            for i in range(j - 1, -1, -1):
                # print(i, j)
                for k in range(i, j + 1):
                    if k == i:
                        dp[i][j] += dp[k + 1][j]
                    elif k == j:
                        dp[i][j] += dp[i][k - 1]
                    else:
                        dp[i][j] += dp[i][k - 1] * dp[k + 1][j]
                # print(dp)
        # print(dp)
        return dp[0][n - 1]


class Solution2:
    def numTrees(self, n: int) -> int:
        """ dp 优化Catalan number
        https://leetcode-cn.com/problems/unique-binary-search-trees/solution/hua-jie-suan-fa-96-bu-tong-de-er-cha-sou-suo-shu-b/
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for k in range(1, i + 1):
                dp[i] += dp[k - 1] * dp[i - k]
        # print(dp)
        return dp[n]