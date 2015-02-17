# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """ bfs 层序遍历：https://leetcode-cn.com/problems/symmetric-tree/solution/dui-cheng-er-cha-shu-cai-yong-ceng-xu-bi-eg8q/ """
        queue = [root]
        level_vals = []
        while queue:
            i = 0
            n = len(queue)
            while i < n:
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    level_vals.append(node.left.val)
                else:
                    level_vals.append(None)
                if node.right:
                    queue.append(node.right)
                    level_vals.append(node.right.val)
                else:
                    level_vals.append(None)
                i += 1
            if level_vals[::-1] != level_vals:
                return False
            level_vals = []
        return True


class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        """ recursive/ dfs: https://leetcode-cn.com/problems/symmetric-tree/solution/dui-cheng-er-cha-shu-by-leetcode-solution/
        时间复杂度：这里遍历了这棵树，渐进时间复杂度为 O(n)O(n)。
        空间复杂度：这里的空间复杂度和递归使用的栈空间有关，这里递归层数不超过 nn，故渐进空间复杂度为 O(n)O(n)。
        空间复杂度见从来不偷懒 的回复

        """
        def dfs(left_root, right_root):
            if not left_root and not right_root:
                return True
            if not (left_root and right_root):
                return False
            if left_root.val != right_root.val:
                return False
            return left_root.val == right_root.val and dfs(left_root.left, right_root.right) and dfs(left_root.right, right_root.left)
        return dfs(root, root)
        """
        my second attempt:
        def dfs(node_left, node_right):
            if not node_left and node_right or (not node_right and node_left):
                return False
            if not node_left and not node_right:
                return True
            if node_left and node_right and node_left.val != node_right.val:
                return False
            return dfs(node_left.left, node_right.right) and dfs(node_left.right, node_right.left)
        return dfs(root.left, root.right)
        """


class Solution3:
    def isSymmetric(self, root: TreeNode) -> bool:
        """ BFS, iterative: https://leetcode-cn.com/problems/symmetric-tree/solution/dong-hua-yan-shi-101-dui-cheng-er-cha-shu-by-user7/
        时间复杂度是 O(n)O(n)，空间复杂度是 O(n)O(n)
        """
        queue = [root, root]
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            if not left and not right:
                continue
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            queue.extend([left.left, right.right, left.right, right.left])
        return True
        """
        # my second attempt
        queue = deque([root, root])
        while queue:
            node_left = queue.popleft()
            node_right = queue.popleft()
            if node_left is None and node_right is not None or node_left is not None and node_right is None :
                return False
            if node_left and node_right and node_left.val != node_right.val:
                return False
            if node_left is None and node_right is None:
                continue
            queue.append(node_left.left)
            queue.append(node_right.right)
            queue.append(node_left.right)
            queue.append(node_right.left)
        return True
        """
