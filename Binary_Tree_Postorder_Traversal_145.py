# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """ recursive solution: https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/er-cha-shu-de-hou-xu-bian-li-by-leetcode-solution/
        时间复杂度：O(n)O(n)，其中 nn 是二叉搜索树的节点数。每一个节点恰好被遍历一次。

        空间复杂度：O(n)O(n)，为递归过程中栈的开销，平均情况下为 O(\log n)O(logn)，最坏情况下树呈现链状，为 O(n)O(n)。

        """
        if not root:
            return []
        res = []
        if root.left:
            res.extend(self.postorderTraversal(root.left))
        if root.right:
            res.extend(self.postorderTraversal(root.right))
        res.append(root.val)
        return res


class Solution2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        栈 + iterative solution: https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/ 此为通解很好理解记忆
        """
        white, grey = 0, 1
        stack = [(root, white)]
        res = []
        while stack:
            node, color = stack.pop()
            if not node:
                continue
            if color == white:
                stack.append((node, grey))
                stack.append((node.right, white))
                stack.append((node.left, white))
            else:
                res.append(node.val)
        return res


class Solution3:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """ morris traversal
        https://www.cnblogs.com/anniekim/archive/2013/06/15/morristraversal.html
        空间复杂度同样是O(1)；时间复杂度也是O(n)，倒序输出过程只不过是加大了常数系数。
        """
        def reverse_traverse(from_node, to_node):
            if from_node == to_node:
                return [from_node.val]
            rt = []
            def reverse(f, t):
                x = f
                y = x.right
                while True:
                    z = y.right
                    y.right = x
                    x = y
                    y = z
                    if x == t:
                        break
            reverse(from_node, to_node)
            curr = to_node
            while True:
                rt.append(curr.val)
                if curr == from_node:
                    break
                curr = curr.right
            reverse(to_node, from_node)
            return rt
        dumb = TreeNode()
        dumb.left = root
        curr = dumb
        res = []
        while curr:
            if not curr.left:
                curr = curr.right
            else:
                pre = curr.left
                while pre.right and pre.right != curr:
                    pre = pre.right
                if not pre.right:
                    pre.right = curr
                    curr = curr.left
                else:
                    res.extend(reverse_traverse(curr.left, pre))
                    pre.right = None
                    curr = curr.right
        return res
