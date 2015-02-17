# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """ DFS; bottom up, recursive: https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xefb4e/  是一种后序遍历. 解：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/solution/er-cha-shu-de-zui-da-shen-du-by-leetcode-solution/
        时间复杂度：O(n)O(n)，其中 nn 为二叉树节点的个数。每个节点在递归中只被遍历一次。

        空间复杂度：O(\textit{height})O(height)，其中 \textit{height}height 表示二叉树的高度。递归函数需要栈空间，而栈空间取决于递归的深度，因此空间复杂度等价于二叉树的高度。

        """
        if not root:
            return 0
        depth_left = self.maxDepth(root.left)
        depth_right = self.maxDepth(root.right)
        return max(depth_left, depth_right) + 1


class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        """
        DFS; top down 是一种前序遍历; recursive: https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xefb4e/
        """
        def top_down(node, depth):
            if not node:
                return depth - 1
            return max(top_down(node.left, depth + 1), top_down(node.right, depth + 1))
        return top_down(root, 1)


class Solution3:
    def maxDepth(self, root: TreeNode) -> int:
        """
        bfs: https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/solution/er-cha-shu-de-zui-da-shen-du-by-leetcode-solution/
        复杂度分析

        时间复杂度：O(n)O(n)，其中 nn 为二叉树的节点个数。与方法一同样的分析，每个节点只会被访问一次。

        空间复杂度：此方法空间的消耗取决于队列存储的元素数量，其在最坏情况下会达到 O(n)O(n)。
        """
        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            i = 0
            n = len(queue)
            while i < n:
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                i += 1
            depth += 1
        return depth
