# Definition for a Node.
# graph
# 图论


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    """ Depth first search / dfs - https://leetcode-cn.com/problems/clone-graph/solution/ke-long-tu-by-leetcode-solution/
    复杂度分析

    时间复杂度：O(N)O(N)，其中 NN 表示节点数量。深度优先搜索遍历图的过程中每个节点只会被访问一次。

    空间复杂度：O(N)O(N)。存储克隆节点和原节点的哈希表需要 O(N)O(N) 的空间，递归调用栈需要 O(H)O(H) 的空间，其中 HH 是图的深度，经过放缩可以得到 O(H) = O(N)O(H)=O(N)，因此总体空间复杂度为 O(N)O(N)。
    """
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        # 如果该节点已经被访问过了，则直接从哈希表中取出对应的克隆节点返回
        if node in self.visited:
            return self.visited[node]
        if not node:
            return node
        # 克隆节点，注意到为了深拷贝我们不会克隆它的邻居的列表
        # 哈希表存储
        # first needs to store cloned node without neighbors, so when recursive calls, it can return without loop infinitely
        self.visited[node] = Node(node.val)
        # 遍历该节点的邻居并更新克隆节点的邻居列表
        for neighbor in node.neighbors:
            cloned_neighbor = self.cloneGraph(neighbor)
            self.visited[node].neighbors.append(cloned_neighbor)
        return self.visited[node]


class Solution2:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        https://leetcode-cn.com/problems/clone-graph/solution/ke-long-tu-by-leetcode-solution/
        复杂度分析

        时间复杂度：O(N)O(N)，其中 NN 表示节点数量。广度优先搜索遍历图的过程中每个节点只会被访问一次。

        空间复杂度：O(N)O(N)。哈希表使用 O(N)O(N) 的空间。广度优先搜索中的队列在最坏情况下会达到 O(N)O(N) 的空间复杂度，因此总体空间复杂度为 O(N)O(N)。

        """
        if not node:
            return node
        # 克隆第一个节点并存储到哈希表中
        visited = {node: Node(node.val)}
        # 将题目给定的节点添加到队列
        nodes = [node]
        # 广度优先搜索
        while nodes:
            # 取出队列的头节点
            curr = nodes.pop(0)
            # 遍历该节点的邻居
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    # 如果没有被访问过，就克隆并存储在哈希表中
                    visited[neighbor] = Node(neighbor.val)
                    # 将邻居节点加入队列中
                    nodes.append(neighbor)
                # 更新当前clone节点的邻居列表
                visited[curr].neighbors.append(visited[neighbor])   
        return visited[node]
