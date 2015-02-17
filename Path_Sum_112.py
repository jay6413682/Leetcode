# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        """ recursive/dfs
        https://leetcode-cn.com/problems/path-sum/solution/lu-jing-zong-he-by-leetcode-solution/
        时间复杂度：O(N)O(N)，其中 NN 是树的节点数。对每个节点访问一次。

        空间复杂度：O(H)O(H)，其中 HH 是树的高度。空间复杂度主要取决于递归时栈空间的开销，最坏情况下，树呈现链状，空间复杂度为 O(N)O(N)。平均情况下树的高度与节点数的对数正相关，空间复杂度为 O(\log N)O(logN)。

        """
        # empty
        if not root:
            return False
        # leaf
        if not root.left and not root.right:
            if targetSum == root.val:
                return True
            else:
                return False
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


class Solution2:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        """
        bfs/iterative/queue: https://leetcode-cn.com/problems/path-sum/solution/lu-jing-zong-he-by-leetcode-solution/
        时间复杂度：O(N)O(N)，其中 NN 是树的节点数。对每个节点访问一次。

        空间复杂度：O(N)O(N)，其中 NN 是树的节点数。空间复杂度主要取决于队列的开销，队列中的元素个数不会超过树的节点数。

        """
        if not root:
            return False
        queue = [root]
        sum_queue = [root.val]
        while queue:
            node = queue.pop(0)
            s = sum_queue.pop(0)
            if not node.left and not node.right and s == targetSum:
                return True
            if node.left:
                queue.append(node.left)
                sum_queue.append(node.left.val + s)
            if node.right:
                queue.append(node.right)
                sum_queue.append(node.right.val + s)
        return False
        '''
        # or
        if not root:
            return False
        queue = deque([(root, targetSum)])
        while queue:
            root, targetSum = queue.popleft()
            if root.left:
                queue.append((root.left, targetSum - root.val))
            if root.right:
                queue.append((root.right, targetSum - root.val))
            if not root.left and not root.right:
                # leaf
                if root.val == targetSum:
                    return True
        return False
        '''
