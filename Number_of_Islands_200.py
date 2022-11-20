class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # flood fill 岛屿问题，类似 https://leetcode.cn/problems/number-of-islands/solution/dao-yu-lei-wen-ti-de-tong-yong-jie-fa-dfs-bian-li-/ Wang Zhengyi 的解 ，我只是多加了个visited 数组
        m = len(grid)
        n = len(grid[0])
        used = [[False for _ in range(n)] for _ in range(m)]
        islands_count = 0
        def dfs(used, i, j):
            # print(used, i, j)
            if used[i][j]:
                return
            if grid[i][j] == '0':
                return
            used[i][j] = True
            directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
            for d in directions:
                new_i = i + d[0]
                new_j = j + d[1]
                if 0 <= new_i <= m - 1 and 0 <= new_j <= n - 1:
                    dfs(used, new_i, new_j)

        for i in range(m):
            for j in range(n):
                if used[i][j]:
                    continue
                if grid[i][j] == '1':
                    dfs(used, i, j)
                    islands_count += 1
        return islands_count
