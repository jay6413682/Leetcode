# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """ my own recursive solution, not efficient...
        图解：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solution/shou-hua-tu-jie-cong-zhong-xu-yu-hou-xu-bian-li-xu/
        已根据https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solution/tu-jie-gou-zao-er-cha-shu-wei-wan-dai-xu-by-user72/ 进行优化，但仍不够
        """
        inorder_num_index_map = {val:i for i, val in enumerate(inorder)}
        if len(postorder) == 1:
            return TreeNode(postorder[-1])
        if not postorder:
            return None
        root_num = postorder[-1]
        # root_index = inorder.index(root_num)
        root_index = inorder_num_index_map[root_num]
        root = TreeNode(root_num)
        left_in_order = inorder[:root_index]
        right_in_order = inorder[root_index + 1:]
        # left_post_order = [num for num in postorder if num in left_in_order]
        left_post_order = postorder[:root_index]
        # right_post_order = [num for num in postorder if num in right_in_order]
        right_post_order = postorder[root_index:-1]
        root.left = self.buildTree(left_in_order, left_post_order)
        root.right = self.buildTree(right_in_order, right_post_order)
        return root


class Solution2:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """ 优化解/通解：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solution/tu-jie-gou-zao-er-cha-shu-wei-wan-dai-xu-by-user72/ """
        inorder_num_index_map = {val:i for i, val in enumerate(inorder)}
        def build(inorder_start, inorder_end, postorder_start, postorder_end):
            if inorder_start > inorder_end or postorder_start > postorder_end:
                return None
            root_index = inorder_num_index_map[postorder[postorder_end]]
            root = TreeNode(inorder[root_index])
            root.left = build(inorder_start, root_index - 1, postorder_start, postorder_start + root_index - inorder_start - 1)
            root.right = build(root_index + 1, inorder_end, postorder_start + root_index - inorder_start, postorder_end - 1)
            return root
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
        '''
        # second try
        inorder_value_index_map = {val: i for i, val in enumerate(inorder)}
        def build(inorder_start, inorder_end, postorder_start, postorder_end):
            if inorder_start > inorder_end or postorder_start > postorder_end:
                return
            inorder_root_index = inorder_value_index_map[postorder[postorder_end]]
            root = TreeNode(inorder[inorder_root_index])
            left_inorder_start = inorder_start
            left_inorder_end = inorder_root_index - 1
            left_postorder_start = postorder_start
            left_postorder_end = postorder_start + (left_inorder_end - left_inorder_start)
            right_inorder_start = inorder_root_index + 1
            right_inorder_end = inorder_end
            right_postorder_start = left_postorder_end + 1
            right_postorder_end = postorder_end - 1
            root.left = build(left_inorder_start, left_inorder_end, left_postorder_start, left_postorder_end)
            root.right = build(right_inorder_start, right_inorder_end, right_postorder_start, right_postorder_end)
            return root

        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
        '''
