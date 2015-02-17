# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """ this solution is similar to https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/solution/tu-jie-er-cha-sou-suo-shu-gou-zao-di-gui-python-go/
        slicing will add time complexity (no much) - o(n * logn) + o(n) = n ?
        another way to get around is to pass both start and end index of nums: https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/solution/jiang-you-xu-shu-zu-zhuan-huan-wei-er-cha-sou-s-33/
        复杂度分析

        时间复杂度：O(n)O(n)，其中 nn 是数组的长度。每个数字只访问一次。

        空间复杂度：O(\log n)O(logn)，其中 nn 是数组的长度。空间复杂度不考虑返回值，因此空间复杂度主要取决于递归栈的深度，递归栈的深度是 O(\log n)O(logn)。

        """
        '''
        n = len(nums)
        if n < 1:
            return None
        mid = (n - 1) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root
        '''
        # 方法一：中序遍历，总是选择中间位置左边的数字作为根节点
        def helper(nums, start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = helper(nums, start, mid - 1)
            root.right = helper(nums, mid + 1, end)
            return root
        return helper(nums, 0, len(nums) - 1)
        '''
        # 方法二：中序遍历，总是选择中间位置右边的数字作为根节点
        # 我的解（麻烦）
        def build(nums, start, end):
            if start > end:
                return
            if start == end - 1:
                root = TreeNode(nums[end])
                root.left = TreeNode(nums[start])
            else:
                mid = (start + end) // 2
                root = TreeNode(nums[mid])
                root.left = build(nums, start, mid - 1)
                root.right = build(nums, mid + 1, end)
            return root
        return build(nums, 0, len(nums) - 1)
        # 官方解
        def build(nums, start, end):
            if start > end:
                return
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = build(nums, start, mid - 1)
            root.right = build(nums, mid + 1, end)
            return root
        return build(nums, 0, len(nums) - 1)
        # 方法三：中序遍历，选择任意一个中间位置数字作为根节点
        def helper(left, right):
            if left > right:
                return None

            # 选择任意一个中间位置数字作为根节点
            mid = (left + right + randint(0, 1)) // 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)

        '''
