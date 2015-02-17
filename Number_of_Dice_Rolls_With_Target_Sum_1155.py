class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        """ Dynamic programming dp 背包问题
        why modulo 109 + 7
        https://www.zhihu.com/question/49374703 
        similar to https://leetcode-cn.com/problems/number-of-dice-rolls-with-target-sum/solution/zuo-ti-guo-cheng-ji-lu-dpjie-fa-by-maverickbytes/ and
        https://leetcode-cn.com/problems/number-of-dice-rolls-with-target-sum/solution/dong-tai-gui-hua-bei-bao-wen-ti-yun-yong-axtf/

        时间复杂度：O(n * m * t)O(n∗m∗t)
        空间复杂度：O(n * t)O(n∗t) 
        """
        # default to 0
        dp = [[0] * (target + 1) for _ in range(d + 1)]
        # print(dp)
        mini = min(f, target)
        mod = 10 ** 9 + 7
        for x in range(1, mini + 1):
            dp[1][x] = 1
        for i in range(d + 1):
            for j in range(target + 1):
                for k in range(1, f + 1):
                    # if j == 0 or i == 0:
                    #    dp[i][j] = 0
                    if j >= k and i >= 1:
                        # print(dp, i, j, k, dp[i][j], dp[i - 1][j - k])
                        dp[i][j] = (dp[i][j] % mod + dp[i - 1][j - k] % mod) % mod
                        # above is equal to dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % mod but it won't overflow
        return dp[d][target]

class Solution2:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        """ dp 背包问题
        similar to https://mp.weixin.qq.com/s?__biz=MzU4NDE3MTEyMA==&mid=2247487587&idx=1&sn=cc18c2e8c3374612113df7ab7fdc8d46&chksm=fd9cbb7ccaeb326a492255d05daf26345d6805c80ab5b08e392ecf37e6ff5471ee950cac4b4b&scene=178&cur_album_id=1751702161341628417#rd
        """
        dp = [[0] * (target + 1) for _ in range(d)]
        for i in range(d):
            for j in range(target + 1):
                # sum == 0
                if j == 0:
                    dp[i][j] = 0
                # 取第一个die
                elif i == 0 and j <= f:
                    dp[i][j] = 1
                elif i >= 1:
                    for k in range(1, f + 1):
                        if j >= k:
                            dp[i][j] += dp[i - 1][j - k]
                            dp[i][j] %= (10**9 + 7)
        return dp[-1][-1]


class Solution3:
    def __init__(self):
        self.res = 0
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """ bracktrack回溯：https://leetcode-cn.com/problems/number-of-dice-rolls-with-target-sum/solution/1155-zhi-tou-zi-de-nchong-fang-fa-by-ly-010f0/
        超时
        """
        def dfs(n, k, target):
            if n == 0 and target == 0:
                self.res += 1
                return
            elif n == 0:
                return
            elif target <= 0:
                return
            for i in range(1, k + 1):
                if target - i < 0 or n < 1:
                    break
                dfs(n - 1, k, target - i)
        dfs(n, k, target)
        return self.res
