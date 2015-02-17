class UnionFind1(object):
    def __init__(self):
        self.fa = {}
        self.edge_to_remove = None
        self.depth = {}

    def add(self, a):
        if a not in self.fa:
            self.fa[a] = a
            self.depth[a] = 1

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x == y:
            self.edge_to_remove = [a, b]
            return
        # union by rank (depth)
        if self.depth[x] <= self.depth[y]:
            self.fa[x] = y
        else:
            self.fa[y] = x
        if self.depth[x] == self.depth[y]:
            self.depth[y] += 1

    def find(self, a):
        if a == self.fa[a]:
            return a
        # path compression optimization
        self.fa[a] = self.find(self.fa[a])
        return self.fa[a]


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """ 并查集union find;我的解
        并查集的时间复杂度是 O(n*α(n)) α(n)~= constants α 为阿克曼函数的反函数。inverse Ackermann function 
        空间复杂度是 O（n）
        王某某回答 追梦人 comment：如果有多个答案，则返回数组 edges 中最后出现的边 --没有体现这个用例
        https://leetcode-cn.com/problems/redundant-connection/solution/rong-yu-lian-jie-by-leetcode-solution-pks2/
        在树上仅增加一条边。顺序遍历，不在union里面的就是这个解。
        """
        uf = UnionFind1()
        for v1, v2 in edges:
            uf.add(v1)
            uf.add(v2)
            uf.union(v1, v2)
            # print(uf.fa, uf.edge_to_remove)
        return uf.edge_to_remove
