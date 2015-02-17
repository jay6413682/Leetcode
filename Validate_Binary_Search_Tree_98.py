# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """ recursive: https://leetcode-cn.com/problems/validate-binary-search-tree/solution/yan-zheng-er-cha-sou-suo-shu-by-leetcode-solution/
        时间复杂度 : O(n)O(n)，其中 nn 为二叉树的节点个数。在递归调用的时候二叉树的每个节点最多被访问一次，因此时间复杂度为 O(n)O(n)。

        空间复杂度 : O(n)O(n)，其中 nn 为二叉树的节点个数。递归函数在递归过程中需要为每一层递归函数分配栈空间，所以这里需要额外的空间且该空间取决于递归的深度，即二叉树的高度。最坏情况下二叉树为一条链，树的高度为 nn ，递归最深达到 nn 层，故最坏情况下空间复杂度为 O(n)O(n)
        """
        def is_valid_bst(root_node, upper, lower):
            if root_node is None:
                return True
            if root_node.val <= lower or root_node.val >= upper:
                return False
            return is_valid_bst(root_node.left, root_node.val, lower) and is_valid_bst(root_node.right, upper, root_node.val)
        return is_valid_bst(root, 2**31, -2**31 - 1)


class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        """ 中序遍历inorder traverse recursive，我的解
        https://leetcode-cn.com/problems/validate-binary-search-tree/solution/98-yan-zheng-er-cha-sou-suo-shu-di-gui-die-dai-xia/
        """
        def inorder_traverse(root):
            res = []
            if root.left:
                res.extend(inorder_traverse(root.left))
            res.append(root.val)
            if root.right:
                res.extend(inorder_traverse(root.right))
            return res
        ordered_vals = inorder_traverse(root)
        print(ordered_vals)
        i = 1
        while i < len(ordered_vals):
            if ordered_vals[i] <= ordered_vals[i - 1]:
                return False
            i += 1
        return True


class Solution3:
    pre = None
    def isValidBST(self, root: TreeNode) -> bool:
        """ inorder traverse / recursive : https://leetcode-cn.com/problems/validate-binary-search-tree/solution/zhong-xu-bian-li-qing-song-na-xia-bi-xu-miao-dong-/
        https://leetcode-cn.com/problems/validate-binary-search-tree/solution/98-yan-zheng-er-cha-sou-suo-shu-di-gui-die-dai-xia/
        """
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        if self.pre and root.val <= self.pre.val: return False
        self.pre = root
        return self.isValidBST(root.right)


class Solution4:
    pre = None
    def isValidBST(self, root: TreeNode) -> bool:
        """ my own iterative inorder traversal solution
        https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/ 此为通解很好理解记忆
        """
        if not root:
            return True
        white, grey = 0, 1
        stack = [(white, root)]
        pre = None
        # can use pre instead of a whole list
        # res = []
        while stack:
            color, node = stack.pop()
            if node:
                if color == white:
                    stack.append((white, node.right))
                    stack.append((grey, node))
                    stack.append((white, node.left))
                else:
                    if pre and node.val <= pre.val: return False
                    pre = node
                    # res.append(node.val)
                    # n = len(res)
                    # if n > 1 and res[-1] <= res[-2]:
                    #    return False
        return True


Solution().isValidBST(TreeNode(2, TreeNode(1), TreeNode(3)))
