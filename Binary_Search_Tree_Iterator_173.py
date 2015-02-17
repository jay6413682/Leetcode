# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    """ recursion:
    https://leetcode-cn.com/problems/binary-search-tree-iterator/solution/er-cha-sou-suo-shu-die-dai-qi-by-leetcod-4y0y/
    复杂度分析

    时间复杂度：初始化需要 O(n)O(n) 的时间，其中 nn 为树中节点的数量。随后每次调用只需要 O(1)O(1) 的时间。

    空间复杂度：O(n)O(n)，因为需要保存中序遍历的全部结果。

    """

    def _inorder_traverse(self, root):
        res = []
        if not root:
            return []
        if root.left:
            res.extend(self._inorder_traverse(root.left))
        res.append(root)
        if root.right:
            res.extend(self._inorder_traverse(root.right))
        return res

    def __init__(self, root: TreeNode):
        self.nodes_list = self._inorder_traverse(root)
        self.len_nodes_list = len(self.nodes_list)
        self.i = 0
        
    def next(self) -> int:
        nxt_val = self.nodes_list[self.i].val
        self.i += 1
        return nxt_val

    def hasNext(self) -> bool:
        if self.i == self.len_nodes_list:
            return False
        return True


class BSTIterator3:
    """ iterative solution /stack/ monotone stack:
    https://leetcode-cn.com/problems/binary-search-tree-iterator/solution/li-kou-jia-jia-jian-dan-yi-dong-de-san-s-kryk/
    space complexity 平均复杂度应该是O(h)
    """

    def __init__(self, root: TreeNode):
        self.white, self.grey = 0, 1
        self.stack = [(self.white, root)]
        
    def next(self) -> int:
        while self.stack:
            color, node = self.stack.pop()
            if node:
                if color == self.white:
                    if node.right:
                        self.stack.append((self.white, node.right))
                    self.stack.append((self.grey, node))
                    if node.left:
                        self.stack.append((self.white, node.left))
                else:
                    return node.val

    def hasNext(self) -> bool:
        return True if self.stack else False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()