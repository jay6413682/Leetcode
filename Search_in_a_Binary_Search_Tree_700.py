# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """ iterative solution: https://leetcode-cn.com/problems/search-in-a-binary-search-tree/solution/er-cha-sou-suo-shu-zhong-de-sou-suo-by-l-d8zi/
        复杂度分析：https://leetcode-cn.com/problems/search-in-a-binary-search-tree/solution/er-cha-sou-suo-shu-zhong-de-sou-suo-by-l-d8zi/
        主定理，Master Theorem, master theory: https://zhuanlan.zhihu.com/p/100531135
        https://www.coursera.org/lecture/algorithmic-toolbox/proof-of-the-master-theorem-7KR1r
        M^{\log_\alpha\!N}=N^{\log_\alpha\!M} 證明： https://zh.wikipedia.org/wiki/%E5%AF%B9%E6%95%B0 
        主定理例子：
        https://www.geeksforgeeks.org/analysis-algorithm-set-4-master-method-solving-recurrences/
        https://www.geeksforgeeks.org/merge-sort/ 
        """
        if not root:
            return None
        node = root
        while node:
            if node.val == val:
                return node
            elif node.val > val:
                node = node.left
            else:
                node = node.right
        return None


class Solution2:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        recursive solution，master theory，主定理，复杂度：https://leetcode-cn.com/problems/search-in-a-binary-search-tree/solution/er-cha-sou-suo-shu-zhong-de-sou-suo-by-l-d8zi/
        """
        if not root:
            return
        if root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
