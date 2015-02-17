# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """ 递归：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/di-gui-he-die-dai-fa-by-hyj8/ 
    master theorem：time complexity: log (n), space complexity：栈，log（n）
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        larger = p.val if p.val > q.val else q.val
        smaller = p.val if larger == q.val else q.val
        if root.val < larger and root.val > smaller or \
                (root.val == smaller and root.val < larger) or \
                    (root.val > smaller and root.val == larger):
            return root
        elif root.val > larger:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)


class Solution2:
    """ 迭代法；https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-26/
    平均时间复杂度应该是o（log（n））最坏复杂度o（n）
    另外，此题还可用236解法 https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-3c/
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        larger = p.val if p.val > q.val else q.val
        smaller = p.val if larger == q.val else q.val
        while True:
            if root.val > larger:
                root = root.left
            elif root.val < smaller:
                root = root.right
            else:
                return root
