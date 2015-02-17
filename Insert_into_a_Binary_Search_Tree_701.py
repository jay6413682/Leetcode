# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """ my iterative solution, similar to https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/solution/er-cha-sou-suo-shu-zhong-de-cha-ru-cao-zuo-by-le-3/
        根据master theorem，time complexity is O(logn), worst time complexity is O(n)
        """
        if not root:
            return TreeNode(val)
        node = root
        prev = None
        while node:
            prev = node
            if node.val < val:
                node = node.right
            else:
                node = node.left
        node = TreeNode(val)
        if prev.val < val:
            prev.right = node
        else:
            prev.left = node
        return root


class Solution2:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """ recursive: https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/solution/di-gui-he-fei-di-gui-liang-chong-fang-shi-jie-jue-/
        """
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
