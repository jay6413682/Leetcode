class UnionFind(object):
    def __init__(self, total):
        self.fa = {num : num for num in range(total)}
        self.counts = {num: 1 for num in range(total)}
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x == y:
            return
        if self.counts[x] >= self.counts[y]:
            self.counts[x] += self.counts[y]
            self.fa[y] = x
        else:
            self.counts[y] += self.counts[x]
            self.fa[x] = y

    def find(self, a):
        if self.fa[a] == a:
            return a
        self.fa[a] = self.find(self.fa[a])
        return self.fa[a]


class Solution:
    """ my solution, 并查集，UnionFind；正向思维
    会超时
    dummy 就是屋顶 与屋顶相连就是与dummy 相连
    原因：
    mrronin/Mr.Ronin：补上被击碎的砖块以后，有多少个砖块因为这个补上的这个砖块而与屋顶的砖块相连 这句话让此问题直接从Hard变为Normal... 正向突破时每一次hit都需要构建一次并查集，大样本时轻易超时 反向则简单的多
    """
    def _one_d_index(self, i, j, length):
        return i * length + j

    def _create_union_find(self, uf, height, length, dummy, grid):
        for i in range(height):
            for j in range(length):
                ij_index = self._one_d_index(i, j, length)
                if grid[i][j] == 1:
                    if i == 0:
                        uf.union(ij_index, dummy)
                    else:
                        if grid[i - 1][j] == 1:
                            uf.union(ij_index, self._one_d_index(i - 1, j, length))
                        if j > 0 and grid[i][j - 1] == 1:
                            uf.union(ij_index, self._one_d_index(i, j - 1, length))
                        # 只需要与左侧和上方做union；不需要右侧和下方，避免重复
                        # if i < height - 1 and grid[i + 1][j] == 1:
                        #    uf.union(ij_index, self._one_d_index(i + 1, j, length))
                        # if j < length - 1 and grid[i][j + 1] == 1:
                        #    uf.union(ij_index, self._one_d_index(i, j + 1, length))
                    '''
                    # 也可只向右侧和下方
                    #print(i, j , x, length, width, dummy)
                    if i == 0:
                        #print(dummy, x)
                        uf.union(dummy, x)
                    if j + 1 < length and grid[i][j + 1] == 1:
                        new_x = self._to_one_dimension(i, j + 1, length)
                        #print(new_x, x)
                        uf.union(x, new_x)
                    if i + 1 < width and grid[i + 1][j] == 1:
                        new_x = self._to_one_dimension(i + 1, j, length)
                        #print(new_x, x)
                        uf.union(x, new_x)
                    '''


    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        res = []
        height = len(grid)
        length = len(grid[0])
        total = height * length
        uf = UnionFind(total + 1)
        dummy = total
        self._create_union_find(uf, height, length, dummy, grid)
        # print(uf.fa, uf.counts)
        stable_brick_counts = uf.counts[uf.find(dummy)]
        for h_i, h_j in hits:
            if grid[h_i][h_j] == 1:
                grid[h_i][h_j] = 0
                # print(grid)
                uf = UnionFind(total + 1)
                self._create_union_find(uf, height, length, dummy, grid)
                # print(uf.fa, uf.counts)
                new_stable_brick_counts = uf.counts[uf.find(dummy)]
                fallen = stable_brick_counts - new_stable_brick_counts
                # 若敲掉的本身就不stable为0
                if fallen == 0:
                    res.append(0)
                else:
                    res.append(fallen - 1)
                stable_brick_counts = new_stable_brick_counts
            else:
                res.append(0)
        return res


class UnionFind(object):
    def __init__(self, total):
        self.fa = {num : num for num in range(total)}
        self.counts = {num: 1 for num in range(total)}
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x == y:
            return
        if self.counts[x] >= self.counts[y]:
            self.counts[x] += self.counts[y]
            self.fa[y] = x
        else:
            self.counts[y] += self.counts[x]
            self.fa[x] = y

    def find(self, a):
        if self.fa[a] == a:
            return a
        self.fa[a] = self.find(self.fa[a])
        return self.fa[a]


class Solution2:
    """ 并查集只能并（加），没有减，所以逆向思维; 先敲掉，求并，再逆向填上，求并，效率高
    dummy 就是屋顶 与屋顶相连就是与dummy 相连
    视频讲解：https://leetcode-cn.com/problems/bricks-falling-when-hit/solution/803-da-zhuan-kuai-by-leetcode-r5kf/
    时间复杂度：O((N + rows * cols) * alpha(rows * cols)，其中 NN 为数组 \textit{hits}hits 的长度，rowsrows 和 colscols 分别为矩阵的行数和列数，使用了路径压缩和按制排序，alpha(rows * cols)；

    空间复杂度：O(rows⋅cols)。
    """
    def _one_d_index(self, i, j, length):
        return i * length + j

    def _create_union_find(self, uf, height, length, dummy, grid):
        for i in range(height):
            for j in range(length):
                ij_index = self._one_d_index(i, j, length)
                if grid[i][j] == 1:
                    if i == 0:
                        uf.union(ij_index, dummy)
                    else:
                        if grid[i - 1][j] == 1:
                            uf.union(ij_index, self._one_d_index(i - 1, j, length))
                        if j > 0 and grid[i][j - 1] == 1:
                            uf.union(ij_index, self._one_d_index(i, j - 1, length))
                        # 只需要与左侧和上方做union；不需要右侧和下方，避免重复
                        # if i < height - 1 and grid[i + 1][j] == 1:
                        #    uf.union(ij_index, self._one_d_index(i + 1, j, length))
                        # if j < length - 1 and grid[i][j + 1] == 1:
                        #    uf.union(ij_index, self._one_d_index(i, j + 1, length))

    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        height = len(grid)
        length = len(grid[0])
        total = height * length
        uf = UnionFind(total + 1)
        dummy = total
        len_hits = len(hits)
        res = [0] * len_hits
        # copy the grid
        grid_copy = [[col for col in row] for row in grid]
        for h_i, h_j in hits:
            # 先打掉
            grid_copy[h_i][h_j] = 0
        # 打掉的做并查集
        self._create_union_find(uf, height, length, dummy, grid_copy)
        # print(uf.fa, uf.counts)
        # 倒着填回来再做并查集
        for i in range(len_hits - 1, -1, -1):
            h_i, h_j = hits[i][0], hits[i][1]
            # 原来是1
            if grid[h_i][h_j] == 1:
                ij_index = self._one_d_index(h_i, h_j, length)
                stable_brick_counts = uf.counts[uf.find(dummy)]
                # 第一行，与dummy 并
                if h_i == 0:
                    uf.union(ij_index, dummy)

                # 再与上下左右并
                if h_i > 0 and grid_copy[h_i - 1][h_j] == 1:
                    uf.union(ij_index, self._one_d_index(h_i - 1, h_j, length))
                if h_j > 0 and grid_copy[h_i][h_j - 1] == 1:
                    uf.union(ij_index, self._one_d_index(h_i, h_j - 1, length))
                if h_i < height - 1 and grid_copy[h_i + 1][h_j] == 1:
                    uf.union(ij_index, self._one_d_index(h_i + 1, h_j, length))
                if h_j < length - 1 and grid_copy[h_i][h_j + 1] == 1:
                    uf.union(ij_index, self._one_d_index(h_i, h_j + 1, length))
                # 填回来
                # print(uf.fa, uf.counts)
                grid_copy[h_i][h_j] = 1
                new_stable_brick_counts = uf.counts[uf.find(dummy)]
                fallen = new_stable_brick_counts - stable_brick_counts
                # 若填上的砖块不stable，stable counts 不变
                if fallen == 0:
                    res[i] = 0
                else:
                    res[i] = fallen - 1
            else:
                res[i] = 0
        return res
