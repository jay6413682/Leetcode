class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        bottom up / dynamic programming
        similar to : https://leetcode-cn.com/problems/min-cost-climbing-stairs/solution/dong-tai-gui-hua-by-liweiwei1419-3/
        """
        n = len(cost)
        # n + 1 的位置 is the top of the floor
        dp = [None] * (n + 1)
        cost.append(0)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n + 1):
            # print(i, dp[i - 1], dp[i - 2], cost[i])
            dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])
        return dp[-1]
        """
        # my own solution, similar to https://leetcode-cn.com/problems/min-cost-climbing-stairs/solution/shi-yong-zui-xiao-hua-fei-pa-lou-ti-by-l-ncf8/
        n = len(cost)
        dp = [None] * (n + 1)
        dp[0] = dp[1] = 0
        for i in range(2, n + 1):
            dp[i] = min(dp[i -1] + cost[i - 1], dp [i - 2] + cost[i - 2])
        return dp[n]
        """
        """
        # 滚动数组 https://leetcode-cn.com/problems/min-cost-climbing-stairs/solution/shi-yong-zui-xiao-hua-fei-pa-lou-ti-by-l-ncf8/
        n = len(cost)
        prev = curr = 0
        for i in range(2, n + 1):
            nxt = min(curr + cost[i - 1], prev + cost[i - 2])
            prev, curr = curr, nxt
        return curr

        """


class Solution2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        top down / memorization
        参见128 Solution4 模版
        """
        n = len(cost)
        mem = [None] * (n + 1)
        cost.append(0)
        def dfs(mem, i):
            if i == 0 or i == 1:
                mem[i] = cost[i]
                return cost[i]
            if mem[i] is not None:
                return mem[i]
            # print(mem, i)
            mem[i] = min(dfs(mem, i - 1), dfs(mem, i - 2)) + cost[i]
            return mem[i]
        
        return dfs(mem, n)
