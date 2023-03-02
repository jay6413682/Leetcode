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


class Solution:
    def climbStairs(self, n: int) -> int:
        """ 矩阵快速幂 斐波那契 fibonacci sequence
        https://leetcode.cn/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/
        如果不太懂，看https://www.desgard.com/algo/docs/part2/ch01/1-quick-pow/ and https://www.desgard.com/algo/docs/part2/ch01/3-matrix-quick-pow/
        所谓斐波那契数列指的是数列：1，1，2，3，5，8，13，21，……。即数列满足递推公式，（f(n) = f(n - 1) + f(n - 2)），用语言描述就是后一项等于前两项和。  https://zhuanlan.zhihu.com/p/26679684
        常数项全为零的线性方程组称为齐次线性方程组:https://blog.csdn.net/li2008kui/article/details/108035143 
        线性方程组，其矩阵方程形式为A X = B 或向量方程形式为x 1 α 1 + x 2 α 2 + ⋯ + x n α n = β https://blog.csdn.net/li2008kui/article/details/108035143 
        线性方程组：https://blog.csdn.net/li2008kui/article/details/107946727 ，https://blog.csdn.net/li2008kui/article/details/108027048 ，https://blog.csdn.net/li2008kui/article/details/108035143 
        向量矩阵：https://www.jianshu.com/p/794c1acc0689 
        单位矩阵：在矩阵的乘法中，有一种矩阵起着特殊的作用，如同数的乘法中的1，这种矩阵被称为单位矩阵。 它是个方阵，从左上角到右下角的对角线（称为主对角线）上的元素均为1。 除此以外全都为0。 根据单位矩阵的特点，任何矩阵与单位矩阵相乘都等于本身，而且单位矩阵因此独特性在高等数学中也有广泛应用。
        """
        def matrix_multiply(m1, m2):
            # matrix 乘法
            y1 = len(m1)
            x1 = len(m1[0])
            x2 = len(m2[0])
            res = [[0 for i in range(x2)] for j in range(y1)]
            for i in range(y1):
                for j in range(x2):
                    for k in range(x1):
                        res[i][j] += m1[i][k] * m2[k][j]
            return res
        def fast_pow(x, n):
            # 矩阵快速幂
            multi = x
            m = len(x)
            res = [[0 for _ in range(m)] for _ in range(m)]
            # 单位矩阵
            for i in range(m):
                for j in range(m):
                    if i == j:
                        res[i][j] = 1
            # print(res)
            while n:
                if n & 1 == 1:
                    res = matrix_multiply(res, multi)
                multi = matrix_multiply(multi, multi)
                # print(multi, res)
                n >>= 1
            return res
        # 注意答案 https://leetcode.cn/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/ 中 传入 的 是 n，不同于 https://www.desgard.com/algo/docs/part2/ch01/3-matrix-quick-pow/ 传入 n - 1，也就是 在进行 等比数列 递推时 ，答案 实际 最后多了 一个 [[f(1)], [f(0)]] = [[1,1], [1,0]] * [[f(0)], [f(-1)]], f(-1)其实是 0，所以 如果 求a 时 传入 n 那么 b = [[1], [0]]。 这也可以通过 例子 验证 ，比如算一下 [[f(3)], [f(2)]] 在 传入 n 或 n - 1 时 b 有 什么 不同
        a = fast_pow([[1, 1], [1, 0]], n - 1)
        # print(a)
        b = [[1], [1]]
        # print(matrix_multiply(a, b))
        return matrix_multiply(a, b)[0][0]


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
