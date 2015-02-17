class Solution:
    cache = {}
    def climbStairs(self, n: int) -> int:
        """ recursive / top down / memorization
        视频： https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/
        以及文字解释:它意味着爬到第 x 级台阶的方案数是爬到第 x - 1 级台阶的方案数和爬到第 x - 2 级台阶的方案数的和。很好理解，因为每次只能爬 1 级或 2 级，所以 f(x) 只能从 f(x - 1) 和 f(x - 2) 转移过来，而这里要统计方案总数，我们就需要对这两项的贡献求和。

        time complexity: O(2^n), space complexity o(n)
        超时;
        其实就是fibonacci sequence问题
        可用cache进行优化: https://leetcode-cn.com/problems/climbing-stairs/solution/yi-bu-bu-tui-dao-chu-lei-fei-bo-la-qi-sh-lxp4/ or https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/  视频
        """
        if n in self.cache:
            return self.cache[n]
        if n == 1:
            return 1
        if n == 2:
            return 2

        total_steps = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.cache[n] = total_steps
        return total_steps


class Solution2:
    def climbStairs(self, n: int) -> int:
        """ 动态规划/fibonacci sequence
        视频： https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/
        以及文字解释
        time complexity: O(n), space complexity o(1)
        其实就是fibonacci sequence问题

        另外还有更数学解法matrix 和 binet's formula. 时间复杂度可到o(logn)
        """
        '''
        if n == 1:
            return 1
        # if n == 1
        dp[0] = 1
        # if n == 2
        dp[1] = 2
        for x in range(2, n):
            dp[x] = dp[x - 1] + dp[x - 2]
        return dp[-1]
        '''
        # optimization:
        if n == 1 or n == 2:
            return n
        first = 1
        second = 2
        for _ in range(3, n + 1):
            res = first + second
            first = second
            second = res
        return res


class Solution3:
    """
    我的dfs解，类似https://leetcode-cn.com/problems/climbing-stairs/solution/yi-bu-bu-tui-dao-chu-lei-fei-bo-la-qi-sh-lxp4/
    复杂度类似solution1
    """
    path_counter = 0

    def climbStairs(self, n: int) -> int:
        def dfs(leftover):
            if leftover < 0:
                return
            elif leftover == 0:
                self.path_counter += 1
                return
            else:
                dfs(leftover - 1)
                dfs(leftover - 2)
        dfs(n)
        return self.path_counter
