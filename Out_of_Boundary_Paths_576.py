class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """ dp https://mp.weixin.qq.com/s?__biz=MzU4NDE3MTEyMA==&mid=2247485426&idx=1&sn=071aec0bf5bc2e20c58f4cbb3dcb0fbc&chksm=fd9cacedcaeb25fb895cb99963dcfcde6b10268893a085eed4000b48bf070cecbdf7c81bf991&token=1934509949&lang=zh_CN&scene=21#wechat_redirect
        通过 dfs signature ：dfs(x, y, steps) ,得到dp[i][j][k]表示从 [i,j] 位置最多移动 k 次能够把小球移出去的最大路径数量。然后确定f[(x,y)][step]=f[(x−1,y)][step−1]+f[(x+1,y)][step−1]+f[(x,y−1)][step−1]+f[(x,y+1)][step−1]
        https://leetcode-cn.com/problems/out-of-boundary-paths/solution/yi-ti-wu-jie-dfs-jian-zhi-ji-yi-hua-sou-k4dtg/ ：
        nextgen7576：请教，既然第三步从第二步来，第二步从第一步来，为什么给tmp赋初始值的时候，要 for (int k = 1; k <= maxMove; k++) 赋值，而不是给k=1赋值就可以了？
        彤丶：对于四条边，他们可以不经过其他任何位置直接走一步越界，所以，每次都要重新初始化，dp针对的是从其他位置转移而来。比如，[0, 1]这个点，不管K等于几，它始终都有一条路径越界，也就是它每一轮的初始值都是1。这地方确实有点绕，仔细琢磨下。中间的位置他们必须经过其他位置才能越界，所以，他们只能通过dp转移而来，或者说他们的初始值是0，Java中正好int类型默认值是0，所以，不用单独再设置了。
        """
        dp = [[[0 for _ in range(maxMove + 1)] for _ in range(n)] for _ in range(m)]
        # print(dp)
        mod = 10**9 + 7
        for k in range(1, maxMove + 1):
            for i in range(m):
                for j in range(n):
                    # print(i, j, k)
                    if i == 0:
                        dp[i][j][k] += 1
                    if j == 0:
                        dp[i][j][k] += 1
                    if i == m - 1:
                        dp[i][j][k] += 1
                    if j == n - 1:
                        dp[i][j][k] += 1
                    if i >= 1:
                        dp[i][j][k] += dp[i - 1][j][k - 1]
                    if j >= 1:
                        dp[i][j][k] += dp[i][j - 1][k - 1]
                    if i + 1 < m:
                        dp[i][j][k] += dp[i + 1][j][k - 1]
                    if j + 1 < n:
                        dp[i][j][k] += dp[i][j + 1][k - 1]
                    dp[i][j][k] %= mod
        # print(dp)
        return dp[startRow][startColumn][maxMove]
