class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """ my most unefficient recursive solution / top down """
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        """ dp 未优化法： https://leetcode-cn.com/problems/unique-paths/solution/bu-tong-lu-jing-by-leetcode-solution-hzjf/
        时间复杂度：O(mn)

        空间复杂度：O(mn)
        """
        """
        if m == 1 or n == 1:
            return 1
        i = 1
        res = [n * [None] for _ in range(m)]
        while i <= m:
            j = 1
            while j <= n:
                if i == 1 or j == 1:
                    res[i - 1][j - 1] = 1
                else:
                    res[i - 1][j - 1] = res[i - 2][j - 1] + res[i - 1][j - 2]
                j += 1
            i += 1
        return res[m - 1][n - 1]
        """
        dp = [[1] * n for _ in range(m)]
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        """ dp 优化 1: https://leetcode-cn.com/problems/unique-paths/solution/dong-tai-gui-hua-by-powcai-2/
        simonffl 的评论
        图解： https://leetcode-cn.com/problems/unique-paths/solution/you-hua-yi-de-tu-jie-by-jet-2/ 
        """
        pre = [1] * n
        curr = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                curr[j] = pre[j] + curr[j - 1]
            pre = curr[:]
        return curr[-1]


class Solution4:
    def uniquePaths(self, m: int, n: int) -> int:
        """ dp 优化 2: https://leetcode-cn.com/problems/unique-paths/solution/dong-tai-gui-hua-by-powcai-2/
        Defias的评论
        """
        curr = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                curr[j] += curr[j - 1]
        return curr[-1]


class Solution5:
    def uniquePaths(self, m: int, n: int) -> int:
        """ 数学组合解：https://leetcode-cn.com/problems/unique-paths/solution/bu-tong-lu-jing-by-leetcode-solution-hzjf/
        python 解 https://leetcode-cn.com/problems/unique-paths/solution/liang-chong-jie-ti-si-lu-dong-tai-gui-hu-onsr/
        一共 m + n - 2 步 想象成 这么多个 不同的空盒子（编号1，2，3 ... m + n - 2） ，选出 m - 1 个 盒子 编号（放向下的步），不考虑顺序 有多少种 选法，这就是求有多少种 组合 https://zhuanlan.zhihu.com/p/41855459
        不要去想 二维 的table，只考虑这些 步如何 选择，因为最后都能从起点到终点
        杨辉三角形（中国古代数学家）（帕斯卡三角形）： https://www.mathsisfun.com/pascals-triangle.html
        table 可以转化成 杨辉三角 ，把table 旋转45度. 画图 比如m=3，n=4，会发现，右下角 是 C(m+n-2, n -1) 
        时间复杂度：O(m)。由于我们交换行列的值并不会对答案产生影响，因此我们总可以通过交换 mm 和 nn 使得 m \leq nm≤n，这样空间复杂度降低至 O(min(m,n))。

        空间复杂度：O(1)

        """
        res = 1
        i = 1
        bigger = m if m > n else n
        smaller = m if bigger == n else n
        j = bigger
        # A(m + n - 2, m - 1) -> n * n + 1 * ... * m + n - 2
        while bigger <= j <= m + n - 2:
            res *= j
            j += 1
        # A(m - 1)
        while 1 <= i <= smaller - 1:
            res //= i
            i += 1
        return int(res)
