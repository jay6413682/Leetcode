class UnionFind(object):
    def __init__(self, city_counts):
        self.fa = {num: num for num in range(city_counts)}
        self.height = {num: 1 for num in range(city_counts)}
        # initially province counts equals city counts
        self.province_counts = city_counts

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x == y:
            return
        # print(a, b, self.fa)
        # only when a and b were not connected but now is connected, then province count - 1
        self.province_counts -= 1
        # union by height
        if x <= y:
            self.fa[x] = y
        else:
            self.fa[y] = x
        if x == y:
            self.height[y] += 1

    def is_connected(self, a, b):
        return self.find(a) == self.find(b)
    def find(self, a):
        if a == self.fa[a]:
            return a
        # path compression
        self.fa[a] = self.find(self.fa[a])
        return self.fa[a]


class Solution:
    """ The following two are the most commonly used representations of a graph. 
    1. Adjacency Matrix 
    2. Adjacency List 
    Adjacency matrix for undirected graph is always symmetric.
    https://www.geeksforgeeks.org/graph-and-its-representations/ 
    这个矩阵是Adjacency matrix for undirected graph
    union find 并查集： similar to https://leetcode-cn.com/problems/number-of-provinces/solution/bing-cha-ji-python-dai-ma-java-dai-ma-by-liweiwei1/
    并查集和人脸聚类有啥关系： https://leetcode-cn.com/problems/number-of-provinces/solution/tu-jie-bing-cha-ji-by-time-limit-6x7p/
    并查集的时间复杂度是 O(n^2α(n))
    空间复杂度是 O（n）
    """
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        height = length = len(isConnected)
        uf = UnionFind(height)
        for i in range(height):
            # only check when i > j is enough, because i < j is the same
            for j in range(i):
                if isConnected[i][j] == 1:
                    # print(i, j)
                    uf.union(i, j)
        return uf.province_counts


class UnionFind2:
    def __init__(self, city_counts):
        self.fa = [k for k in range(city_counts)]
        self.depth = {k: 1 for k in range(city_counts)}

    def union(self, i, j):
        fa_i = self.find(i)
        fa_j = self.find(j)
        if fa_i == fa_j:
            return
        self.fa[fa_i] = fa_j
        '''
        if self.depth[fa_i] < self.depth[fa_j]:
            self.fa[fa_i] = fa_j
            self.depth[fa_j] += 1
        else:
            self.fa[fa_j] = fa_i
            self.depth[fa_i] += 1
        '''


    def find(self, x):
        if self.fa[x] != x:
            fa_fa = self.find(self.fa[x])
            # self.fa[x] = fa_fa
        else:
            fa_fa = x
        return fa_fa

class Solution2:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """ UnionFind 如果不做任何优化 """
        n = len(isConnected[0])
        uf = UnionFind2(n)
        for i in range(n):
            for j in range(i, n):
                if isConnected[i][j]:
                    uf.union(i, j)
        provinces = set()
        for i in range(n):
            fa_fa = uf.find(i)
            # print(i, fa_fa)
            provinces.add(fa_fa)
        # print(provinces)
        return len(provinces)
