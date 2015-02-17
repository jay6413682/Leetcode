# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """ 类似106 题通解：通解：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solution/tu-jie-gou-zao-er-cha-shu-wei-wan-dai-xu-by-user72/
        复杂度https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/cong-qian-xu-yu-zhong-xu-bian-li-xu-lie-gou-zao-9/
        时间复杂度：O(n)O(n)，其中 nn 是树中的节点个数。

        空间复杂度：O(n)O(n)，除去返回的答案需要的 O(n)O(n) 空间之外，我们还需要使用 O(n)O(n) 的空间存储哈希映射，以及 O(h)O(h)（其中 hh 是树的高度）的空间表示递归时栈空间。这里 h < nh<n，所以总空间复杂度为 O(n)O(n)。
        迭代 栈解：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--22/
        inorder = [ 20, 9, 15, 3, 7 ]: 第一个20一定是最左的node； 所以当inorder 的 20 与preorder 的 20 相等时，最左相等，下一个9也相等，9是20的parent；再下一个15不等于3，15一定是9的右子树不是9的parent （只有这两种可能）
        preorder = [3, 9, 20, 15, 7 ]
        思路可以看看，但是很复杂，了解一下思路罢了
        """
        inorder_val_index_map = {val: i for i, val in enumerate(inorder)}
        def build(preorder_start, preorder_end, inorder_start, inorder_end):
            if preorder_start > preorder_end or inorder_start > inorder_end:
                return None
            root_index = inorder_val_index_map[preorder[preorder_start]]
            root = TreeNode(inorder[root_index])
            root.left = build(preorder_start + 1, preorder_start + root_index - inorder_start, inorder_start, root_index - 1)
            root.right = build(preorder_start + root_index -inorder_start + 1, preorder_end, root_index + 1, inorder_end)
            return root
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
