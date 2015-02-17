class Solution:
    def __init__(self):
        self.res = -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        backtrack 回溯法 超时
        similar to https://leetcode-cn.com/problems/coin-change/solution/javadi-gui-ji-yi-hua-sou-suo-dong-tai-gui-hua-by-s/
        """
        def backtrack(amount, depth, start):
            # 剪枝
            if self.res != -1 and depth >= self.res:
                return
            if amount == 0:
                if self.res == -1:
                    self.res = depth
                else:
                    self.res = depth if depth < self.res else self.res
            if amount < 0:
                return
            for i, c in enumerate(coins):
                # 剪枝
                if i < start:
                    continue
                backtrack(amount - c, depth + 1, i)
        backtrack(amount, 0, 0)
        return self.res


class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """ top down / memorization python超时。。。（java不超时）
        参见128 Solution4 模版
        similar to https://leetcode-cn.com/problems/coin-change/solution/javadi-gui-ji-yi-hua-sou-suo-dong-tai-gui-hua-by-s/ 
        https://leetcode-cn.com/problems/coin-change/solution/322-ling-qian-dui-huan-by-leetcode-solution/ python解 不超时
        """
        mem = [-1] * (amount + 1)
        def dfs(amount):
            if amount == 0:
                mem[amount] = 0
                return 0
            if amount < 0:
                return -1
            if mem[amount] != -1:
                return mem[amount]
            for c in coins:
                raw = dfs(amount - c)
                # print(amount, c, raw, mem)
                if (mem[amount] == -1 and raw != -1) or (raw >= 0 and raw < mem[amount]):
                    mem[amount] = raw + 1
            return mem[amount]
        return dfs(amount)
    # '''
    '''
    # https://leetcode-cn.com/problems/coin-change/solution/322-ling-qian-dui-huan-by-leetcode-solution/ 优化解
    def coinChange(self, coins: List[int], amount: int) -> int:
        @functools.lru_cache(amount)
        def dp(rem) -> int:
            if rem < 0: return -1
            if rem == 0: return 0
            mini = int(1e9)
            for coin in self.coins:
                res = dp(rem - coin)
                if res >= 0 and res < mini:
                    mini = res + 1
            return mini if mini < int(1e9) else -1

        self.coins = coins
        if amount < 1: return 0
        return dp(amount)
    '''



class Solution3:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """ bottom up / dp
        similar to https://leetcode-cn.com/problems/coin-change/solution/javadi-gui-ji-yi-hua-sou-suo-dong-tai-gui-hua-by-s/
        and https://leetcode-cn.com/problems/coin-change/solution/322-ling-qian-dui-huan-by-leetcode-solution/
        复杂度分析

        时间复杂度：O(Sn)O(Sn)，其中 SS 是金额，nn 是面额数。我们一共需要计算 O(S)O(S) 个状态，SS 为题目所给的总金额。对于每个状态，每次需要枚举 nn 个面额来转移状态，所以一共需要 O(Sn)O(Sn) 的时间复杂度。
        空间复杂度：O(S)O(S)。数组 \textit{dp}dp 需要开长度为总金额 SS 的空间。

        """
        dp = [-1] * (amount + 1)
        for i in range(amount + 1):
            for c in coins:
                if i == 0:
                    dp[i] = 0
                elif i == c:
                    dp[i] = 1
                elif i > c and dp[i - c] != -1:
                    raw = dp[i - c]
                    if raw + 1 < dp[i] or dp[i] == -1:
                        dp[i] = raw + 1
        return dp[-1]


class Solution4:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """ dp/背包问题 超时
        https://leetcode-cn.com/problems/coin-change/solution/dong-tai-gui-hua-bei-bao-wen-ti-zhan-zai-3265/ 
        时间复杂度：共有 n * cntn∗cnt 个状态需要转移，每个状态转移最多遍历 cntcnt 次。整体复杂度为 O(n * cnt^2)O(n∗cnt 2)。
        空间复杂度：O(n * cnt)O(n∗cnt)。

        """
        m = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(amount + 1):
                if i == 0 and j == 0:
                    dp[0][0] = 0
                elif i != 0:
                    for k in range(j // coins[i - 1] + 1):
                        if dp[i][j] == -1 and dp[i - 1][j - k * coins[i - 1]] != -1:
                            dp[i][j] = dp[i - 1][j - k * coins[i - 1]] + k
                        if dp[i][j] != -1 and dp[i - 1][j - k * coins[i - 1]] != -1:
                            dp[i][j] = min(dp[i][j], dp[i - 1][j - k * coins[i - 1]] + k)
        return dp[-1][-1]


class Solution5:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """ dp/背包问题 ， 优化后 https://leetcode-cn.com/problems/coin-change/solution/dong-tai-gui-hua-bei-bao-wen-ti-zhan-zai-3265/
        时间复杂度：共有 n * cntn∗cnt 个状态需要转移，整体复杂度为 O(n * cnt)O(n∗cnt)。
        空间复杂度：O(cnt)O(cnt)。
        """
        m = len(coins)
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(m + 1):
            for j in range(amount + 1):
                if i != 0 and j - coins[i - 1] >= 0:
                    if dp[j] == -1 and dp[j - coins[i - 1]] != -1:
                        dp[j] = dp[j - coins[i - 1]] + 1
                    if dp[j] != -1 and dp[j - coins[i - 1]] != -1:
                        dp[j] = min(dp[j], dp[j - coins[i - 1]] + 1)
        return dp[-1]
