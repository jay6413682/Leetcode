from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """ recursive solution : 未优化： https://leetcode-cn.com/problems/minimum-path-sum/solution/dong-tai-gui-hua-he-di-gui-liang-chong-fang-shi-tu/"""
        '''
        m = len(grid) - 1
        n = len(grid[0]) - 1
        if m == 0:
            return sum(grid[0][:])
        elif n == 0:
            return sum([x[0] for x in grid])
        # list comprehension 和 local variable scope 不同：https://stackoverflow.com/questions/13905741/accessing-class-variables-from-a-list-comprehension-in-the-class-definition
        return min(self.minPathSum(grid[:m][:]) + grid[m][n], self.minPathSum((lambda n=n, grid=grid: [x[:n] for x in grid])()) + grid[m][n])
        '''
        def min_path_sum(grid, i, j):
            if i == 0 and j == 0:
                return grid[i][j]
            if i == 0:
                return grid[i][j] + min_path_sum(grid, i, j - 1)
            if j == 0:
                return grid[i][j] + min_path_sum(grid, i - 1, j)
            return min(min_path_sum(grid, i, j - 1), min_path_sum(grid, i - 1, j)) + grid[i][j]
        return min_path_sum(grid, len(grid) - 1, len(grid[0]) - 1)


class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """ dp 优化解： https://leetcode-cn.com/problems/minimum-path-sum/solution/zui-xiao-lu-jing-he-by-leetcode-solution/ 
        时间复杂度：O(mn)O(mn)，其中 mm 和 nn 分别是网格的行数和列数。需要对整个网格遍历一次，计算 \textit{dp}dp 的每个元素的值。
        空间复杂度：空间复杂度可以优化，例如每次只存储上一行的 \textit{dp}dp 值，则可以将空间复杂度优化到 O(n)O(n)。

        """
        minimum_sum_up_row = [None] * len(grid[0])
        minimum_sum_up_row[0] = grid[0][0]
        res = 0
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if i == 0 and j > 0:
                    minimum_sum_up_row[j] = minimum_sum_up_row[j - 1] + num
                elif j == 0 and i > 0:
                    minimum_sum_up_row[j] = minimum_sum_up_row[j] + num
                elif j > 0 and i > 0:
                    minimum_sum_up_row[j] = min(minimum_sum_up_row[j], minimum_sum_up_row[j - 1]) + num
        return minimum_sum_up_row[-1]


class Solution3:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """ dp 优化解： https://leetcode-cn.com/problems/minimum-path-sum/solution/zui-xiao-lu-jing-he-dong-tai-gui-hua-gui-fan-liu-c/
        时间复杂度 O(M \times N)O(M×N) ： 遍历整个 gridgrid 矩阵元素。
        空间复杂度 O(1)O(1) ： 直接修改原矩阵，不使用额外空间。
        """
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if i == 0 and j > 0:
                    grid[i][j] = grid[i][j - 1] + num
                elif j == 0 and i > 0:
                    grid[i][j] = grid[i - 1][j] + num
                elif j > 0 and i > 0:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + num
        return grid[-1][-1]


class Solution4:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """ dynamic programming; no optimization """
        m = len(grid)
        n = len(grid[0])
        dp = [[None] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
        return dp[m - 1][n - 1]


class Solution5:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        top down / memorization
        参见128 Solution4 模版
        """
        m = len(grid)
        n = len(grid[0])
        mem = [[None] * n for _ in range(m)]
        def dfs(i, j, mem):
            if mem[i][j] is not None:
                return mem[i][j]
            if i == 0 and j == 0:
                mem[i][j] = grid[i][j]
                return mem[i][j]
            if i == 0:
                mem[i][j] = dfs(i, j - 1, mem) + grid[i][j]
                return mem[i][j]
            if j == 0:
                mem[i][j] = dfs(i - 1, j, mem) + grid[i][j]
                return mem[i][j]
            mem[i][j] = min(dfs(i - 1, j, mem), dfs(i, j - 1, mem)) + grid[i][j]
            return mem[i][j]
        return dfs(m - 1, n - 1, mem)


print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
