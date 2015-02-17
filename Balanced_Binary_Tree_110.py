# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """ my solution, top down, BSF, iterative, https://leetcode-cn.com/problems/balanced-binary-tree/solution/110-ping-heng-er-cha-shu-by-fantacy-y2kn/
        """
        def get_height(node):
            if not node:
                return 0
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            return left_height + 1 if left_height > right_height else right_height + 1
        if not root:
            return True
        queue = [root]
        while queue:
            node = queue.pop()
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            # print('left_height: {}, right_height: {}'.format(left_height, right_height))
            if abs(left_height - right_height) > 1:
                return False
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return True


class Solution3:
    balanced = True
    def isBalanced(self, root: TreeNode) -> bool:
        """ bottom up, recursive, dfs, close to https://leetcode-cn.com/problems/balanced-binary-tree/solution/di-gui-qiu-jie-by-fizz_2021-6hky/
        complexity: https://leetcode-cn.com/problems/balanced-binary-tree/solution/ping-heng-er-cha-shu-by-leetcode-solution/
        时间复杂度：O(n)O(n)，其中 nn 是二叉树中的节点个数。使用自底向上的递归，每个节点的计算高度和判断是否平衡都只需要处理一次，        最坏情况下需要遍历二叉树中的所有节点，因此时间复杂度是 O(n)O(n)。

        空间复杂度：O(n)O(n)，其中 nn 是二叉树中的节点个数。空间复杂度主要取决于递归调用的层数，递归调用的层数不会超过 nn。
        """
        def height(root):
            if not root:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            if abs(left_height - right_height) > 1:
                self.balanced = False
            return max(left_height, right_height) + 1
        height(root)
        return self.balanced


class Solution2:
    def isBalanced(self, root: TreeNode) -> bool:
        """ isBalanced: top down （前序遍历）; get_height(高度): bottom up, recursive, dfs, 重复遍历不efficient https://leetcode-cn.com/problems/balanced-binary-tree/solution/ping-heng-er-cha-shu-by-leetcode-solution/
        时间复杂度：O(n^2)，其中 nn 是二叉树中的节点个数。
        最坏情况下，二叉树是满二叉树，需要遍历二叉树中的所有节点，时间复杂度是 O(n)O(n)。
        对于节点 pp，如果它的高度是 dd，则 \texttt{height}(p)height(p) 最多会被调用 dd 次（即遍历到它的每一个祖先节点时）。对于平均的情况，一棵树的高度 hh 满足 O(h)=O(\log n)O(h)=O(logn)，因为 d \leq hd≤h，所以总时间复杂度为 O(n \log n)O(nlogn)。对于最坏的情况，二叉树形成链式结构，高度为 O(n)O(n)，此时总时间复杂度为 O(n^2)。
        空间复杂度：O(n)O(n)，其中 nn 是二叉树中的节点个数。空间复杂度主要取决于递归调用的层数，递归调用的层数不会超过 nn。

        """
        def get_height(node):
            """ bottom up """
            if not node:
                return 0
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            return left_height + 1 if left_height > right_height else right_height + 1
        if not root:
            return True
        return abs(get_height(root.left) - get_height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    my solution. top down. 深度
    """
    is_balanced = True
    def isBalanced(self, root: TreeNode) -> bool:
        def get_max_depth(root, depth):
            # depth 是root 的深度，return 树顶经过该root最大深度
            if not root:
                return depth - 1
            left_max_depth = get_max_depth(root.left, depth + 1)
            right_max_depth = get_max_depth(root.right, depth + 1)
            if abs(left_max_depth - right_max_depth) > 1:
                self.is_balanced = False
            # return max depth
            return max(left_max_depth, right_max_depth)
        get_max_depth(root, 1)
        return self.is_balanced
