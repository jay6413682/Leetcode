
class Solution:

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        flood fill/dfs
        similar to https://leetcode-cn.com/problems/surrounded-regions/solution/dfs-bing-cha-ji-java-by-liweiwei1419/
        """
        def dfs(r, c):
            # convert 'O' to '-' in 4 directions
            if r >= width or r < 0 or c >= length or c < 0:
                return
            if board[r][c] == 'X' or board[r][c] == '-':
                return
            if board[r][c] == 'O':
                board[r][c] = '-'
            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
            for d in directions:
                new_r = r + d[0]
                new_c = c + d[1]
                dfs(new_r, new_c)
        width = len(board)
        length = len(board[0])
        # flood fill boundaries
        for i in range(width):
            for j in range(length):
                if i == 0:
                    dfs(i, j)
                elif j == 0:
                    dfs(i, j)
                elif i == width - 1:
                    dfs(i, j)
                elif j == length - 1:
                    dfs(i, j)
        # print(board)
        for i in range(width):
            for j in range(length):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '-':
                    board[i][j] = 'O'
        return board


class Solution2:

    def solve(self, board: List[List[str]]) -> None:
        """
        flood fill/bfs
        similar to https://leetcode-cn.com/problems/surrounded-regions/solution/dfs-bing-cha-ji-java-by-liweiwei1419/
        """
        width = len(board)
        length = len(board[0])
        # flood fill boundaries
        queue = deque()
        for i in range(width):
            for j in range(length):
                if i == 0 and board[i][j] == 'O' or\
                        j == 0 and board[i][j] == 'O' or\
                    i == width - 1 and board[i][j] == 'O' or\
                        j == length - 1 and board[i][j] == 'O':
                    board[i][j] = '-'
                    queue.append((i, j))
        # print(queue)
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while queue:
            r, c = queue.popleft()
            for d in directions:
                new_r = r + d[0]
                new_c = c + d[1]
                if 0 < new_r < width and 0 < new_c < length and board[new_r][new_c] == 'O':
                    board[new_r][new_c] = '-'
                    queue.append((new_r, new_c))
        # print(board)
        for i in range(width):
            for j in range(length):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '-':
                    board[i][j] = 'O'
        return board


class UnionFind(object):
    def __init__(self, total):
        self.fa = {num: num for num in range(total)}
        self.rank = {num: 1 for num in range(total)}

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x == y:
            return
        # union by depth
        if self.rank[x] >= self.rank[y]:
            self.fa[y] = x
        else:
            self.fa[x] = y
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def find(self, num):
        if num == self.fa[num]:
            return num
        # path compression optimization
        self.fa[num] = self.find(self.fa[num])
        return self.fa[num]


class Solution3:
    def _is_on_boarder(self, x, y, width, length):
        if x == 0 or y == 0 or x == width - 1 or y == length - 1:
            return True
        return False

    def _1d_index(self, x, y, length):
        return x * length + y

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        silimar to solution: https://leetcode-cn.com/problems/surrounded-regions/solution/bfsdi-gui-dfsfei-di-gui-dfsbing-cha-ji-by-ac_pipe/
        时间复杂度：O(MN \times \alpha(MN))O(MN×α(MN))，其中 MM 和 NN 分别为行数和列数。注意当使用路径压缩（见 find 函数）和按秩合并（见数组 rank）实现并查集时，单次操作的时间复杂度为 \alpha(MN)α(MN)，其中 \alpha(x)α(x) 为反阿克曼函数，当自变量 xx 的值在人类可观测的范围内（宇宙中粒子的数量）时，函数 \alpha(x)α(x) 的值不会超过 55，因此也可以看成是常数时间复杂度。

        空间复杂度：O(MN)O(MN)，这是并查集需要使用的空间。
        (https://leetcode-cn.com/problems/surrounded-regions/solution/dfs-bing-cha-ji-java-by-liweiwei1419/)

        Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.:
        凡是与边界‘O’相连的‘O’不会flip成‘X’，否则flip: connect all 'O' on border to dummy, connect other 'O' together 
        一维化解决二维数组问题

        """
        width = len(board)
        length = len(board[0])
        total = width * length + 1
        dummy = total - 1
        uf = UnionFind(total)
        for i in range(width):
            for j in range(length):
                if board[i][j] == 'O':
                    ind = self._1d_index(i, j, length)
                    if self._is_on_boarder(i, j, width, length):
                        uf.union(dummy, ind)
                    else:
                        if board[i - 1][j] == 'O':
                            uf.union(self._1d_index(i - 1, j, length), ind)
                        if board[i][j - 1] == 'O':
                            uf.union(self._1d_index(i, j - 1, length), ind)
                        if board[i][j + 1] == 'O':
                            uf.union(self._1d_index(i, j + 1, length), ind)
                        if board[i + 1][j] == 'O':
                            uf.union(self._1d_index(i + 1, j, length), ind)
        # print(uf.fa)
        for i in range(width):
            for j in range(length):
                if uf.find(self._1d_index(i, j, length)) != uf.find(dummy):
                    board[i][j] = 'X'
