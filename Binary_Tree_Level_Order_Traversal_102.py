# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """ BFS solution: https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/bfs-de-shi-yong-chang-jing-zong-jie-ceng-xu-bian-l/
        模版：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/tao-mo-ban-bfs-he-dfs-du-ke-yi-jie-jue-by-fuxuemin/
        复杂度：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/er-cha-shu-de-ceng-xu-bian-li-by-leetcode-solution/
        记树上所有节点的个数为 nn。

        时间复杂度：每个点进队出队各一次，故渐进时间复杂度为 O(n)O(n)。
        空间复杂度：队列中元素的个数不超过 nn 个，故渐进空间复杂度为 O(n)O(n)。

        """
        if not root:
            return []
        res = [[root.val]]
        queue = [root]
        while queue:
            n = len(queue)
            i = 0
            level_res = []
            while i < n:
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    level_res.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    level_res.append(node.right.val)
                i += 1
            if level_res:
                res.append(level_res)
        return res
