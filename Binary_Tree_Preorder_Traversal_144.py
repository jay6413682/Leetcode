# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """ recursive solution: https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/er-cha-shu-de-qian-xu-bian-li-by-leetcode-solution/
        时间复杂度：O(n)，其中 n 是二叉树的节点数。每一个节点恰好被遍历一次。

        空间复杂度：O(n)，为递归过程中栈的开销，平均情况下为 O(logn)，最坏情况下树呈现链状，为 O(n)。
        """
        res = []
        if root:
            res.append(root.val)
            if root.left:
                res.extend(self.preorderTraversal(root.left))
            if root.right:
                res.extend(self.preorderTraversal(root.right))
        return res


class Solution4:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """ 颜色标记+stack + iterative 通解：
        https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/
        """
        white, grey = 0, 1
        stack = [(white, root)]
        res = []
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color == white:
                stack.append((white, node.right))
                stack.append((white, node.left))
                stack.append((grey, node))
            else:
                res.append(node.val)
        return res


class Solution2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """ stack + iterative solution: https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/leetcodesuan-fa-xiu-lian-dong-hua-yan-shi-xbian-2/
        复杂度：https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/er-cha-shu-de-qian-xu-bian-li-by-leetcode-solution/
        时间复杂度：O(n)，其中 nn 是二叉树的节点数。每一个节点恰好被遍历一次。

        空间复杂度：O(n)，为迭代过程中显式栈的开销，平均情况下为 O(\log n)O(logn)，最坏情况下树呈现链状，为 O(n)O(n)。
        """
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


class Solution3:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """ Morris Traversal https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/er-cha-shu-de-qian-xu-bian-li-by-leetcode-solution/
        空间复杂度：O(1)，因为只用了两个辅助指针。

        时间复杂度：O(n)。
        """
        res = []
        curr = root
        while curr:
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right is not None and pre.right is not curr:
                    pre = pre.right
                if pre.right is None:
                    res.append(curr.val)
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    curr = curr.right
        return res
