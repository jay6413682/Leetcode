# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Edge(object):
    def __init__(self, to=None, nxt=None):
        self.to = to
        self.nxt = nxt

class Solution:
    def add(self, heads, edges, fm, to):
        # 添加一条边fm--to
        edge = Edge()
        edge.to = to
        edge.nxt = heads[fm]
        edges.append(edge)
        heads[fm] = len(edges) - 1


    def dfs_preorder_traverse_tree(self, root, edges, head):
        if not root:
            return
        if root.left:
            # 添加边
            self.add(head, edges, root.val, root.left.val)
            # 添加反向边
            self.add(head, edges, root.left.val, root.val)
            self.dfs_preorder_traverse_tree(root.left, edges, head)
        if root.right:
            self.add(head, edges, root.val, root.right.val)
            self.add(head, edges, root.right.val, root.val)
            self.dfs_preorder_traverse_tree(root.right, edges, head)

    def bfs_find(self, target, k, edges, heads):
        visited = set([target.val])
        queue = deque([target.val])
        level = 0
        res = []
        while queue:
            size = len(queue)
            while size:
                cur = queue.popleft()
                if level == k:
                    res.append(cur)
                # traverse 链式向前星
                edge = edges[heads[cur]]
                while True:
                    to = edge.to
                    if to not in visited:
                        visited.add(to)
                        queue.append(to)
                    if edge.nxt == -1:
                        break
                    edge = edges[edge.nxt]
                size -= 1
            # print(queue)
                
            if level == k:
                break
            level += 1
        return res

    def dfs_find(self, cur, k, edges, heads, res, visited):
        if k == 0:
            res.append(cur)
            return
        edge = edges[heads[cur]]
        while True:
            to = edge.to
            if to not in visited:
                visited.add(to)
                self.dfs_find(to, k - 1, edges, heads, res, visited)
            if edge.nxt == -1:
                break
            edge = edges[edge.nxt]

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """ 图，dfs，bfs
        树是一类特殊的图，我们可以通过将二叉树转换为无向图的形式，再进行「BFS / 迭代加深」。
        解法：https://leetcode.cn/problems/all-nodes-distance-k-in-binary-tree/solution/gong-shui-san-xie-yi-ti-shuang-jie-jian-x6hak/ 

        链式前向星存图: https://www.bilibili.com/read/cv13449207 图解
        https://blog.csdn.net/sugarbliss/article/details/86495945 
        Next，表示与这个边起点相同的上一条边的编号。
        head[ i ]数组，表示以 i 为起点的最后一条边的编号。
        """
        heads = [-1] * 500
        edges = []
        self.dfs_preorder_traverse_tree(root, edges, heads)
        # print(edges, head)
        if not edges:
            return []
        # return self.bfs_find(target, k, edges, heads)
        res = []
        self.dfs_find(target.val, k, edges, heads, res, set([target.val]))
        return res
