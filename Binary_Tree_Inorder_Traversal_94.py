# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """ recursive:  中序遍历
        https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/er-cha-shu-de-zhong-xu-bian-li-by-leetcode-solutio/
        时间复杂度：O(n)O(n)，其中 nn 为二叉树节点的个数。二叉树的遍历中每个节点会被访问一次且只会被访问一次。

        空间复杂度：O(n)O(n)。空间复杂度取决于递归的栈深度，而栈深度在二叉树为一条链的情况下会达到 O(n)O(n) 的级别。
        """
        res = []
        if root:
            if root.left:
                res.extend(self.inorderTraversal(root.left))
            res.append(root.val)
            if root.right:
                res.extend(self.inorderTraversal(root.right))
        return res


class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """ 栈 + iterative solution: https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/ 此为通解很好理解记忆
        grant: 其实这种方法的本质是每个节点都要入栈两次后才能访问其元素值，第一次入栈是不能访问其值的，因为第一次入栈是第一次访问该节点，需要先访问该节点的左子树，这时会把该结点和左子树都入栈，所以第二次出栈就可以访问该结点的值啦
        我的理解：可以想像成 grey 是 recursive solution中 的res.append(root),root.left 和root.right 都不是 这一个recursive stack frame应该处理的，所以都是白色
        """
        if not root:
            return []
        white, grey = 0, 1
        stack = [(white, root)]
        res = []
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color == white:
                stack.append((white, node.right))
                stack.append((grey, node))
                stack.append((white, node.left))
            else:
                res.append(node.val)
        return res


class SolutionTwo:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """ iterative/binary tree
        https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/dong-hua-yan-shi-94-er-cha-shu-de-zhong-xu-bian-li/
        dfs(root.left)
            dfs(root.left)
                dfs(root.left)
                    为null返回
                打印节点
                dfs(root.right)
                    dfs(root.left)
                        dfs(root.left)
                ........

        https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/leetcodesuan-fa-xiu-lian-dong-hua-yan-shi-xbian-2/
        """
        stack = deque()
        rt = root
        res = []
        while rt or stack:
            # 先到最左；并压入栈
            while rt:
                stack.append(rt)
                rt = rt.left
            # 弹出栈顶 - 最左，放入res
            node = stack.pop()
            res.append(node.val)
            # 如果最左有右子树，移到右子树，循环
            if node.right:
                rt = node.right
        return res


class Solution3:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """ Morris Traversal https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/er-cha-shu-de-qian-xu-bian-li-by-leetcode-solution/
        前驱节点/predecessor/后继节点/successor https://www.jianshu.com/p/5a80531ef63 只應用於中序遍历
        What is Predecessor and Successor : When you do the inorder traversal of a binary tree, the neighbors of given node are called Predecessor(the node lies behind of given node) and Successor (the node lies ahead of given node).
        前驱节点：当前节点左子树的最右节点（例如1节点的前驱节点为5），若无左子树，则：当前节点是其父节点的右子树（5节点的前驱节点为2）；

        后继节点：当前节点右子树的最左节点（1节点的后继节点为6），若无右子树，则：当前节点为其父节点的左子树（6节点的后继节点为3）。

        可以想象成寻找predecessor 前驱节点的过程； 比如https://stackoverflow.com/questions/5502916/explain-morris-inorder-tree-traversal-without-using-stacks-or-recursion 解答的图
        res 是一个list，X的前一个元素是B, Y 的前一个元素是A，A没有前一个元素（A是第一个元素）；Y的后一个元素是 B（后继节点），X的后继节点是C：[A, Y, B, X，C。。。]
        所以关键是把某节点的前驱节点和该节点连起来：B->X，A->Y连起来；因为中序遍历时root 左子树 在res 中 root的左侧，右子树在res 中 root的右侧，所以当root 进入res 之后，跳到root = root.right
        空间复杂度：O(1)，因为只用了两个辅助指针。

        时间复杂度：O(n)。
        """
        curr = root
        res = []
        while curr:
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            else:
                # pre 是curr前驱节点
                pre = curr.left
                while pre.right and pre.right != curr:
                    pre = pre.right
                if not pre.right:
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    res.append(curr.val)
                    curr = curr.right
        return res
