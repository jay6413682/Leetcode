# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ DFS, my own solution, very inefficient """
        roots_p = []
        roots_q = []
        def traverse(root, end_node):
            traversed = []
            if root:
                traversed.append(root)
                if root.val == end_node.val:
                    return traversed
                if root.left:
                    traversed.extend(traverse(root.left, end_node))
                    if traversed[-1].val == end_node.val:
                        return traversed
                    else:
                        traversed = [root]
                if root.right:
                    traversed.extend(traverse(root.right, end_node))
                    if traversed[-1].val == end_node.val:
                        return traversed
            return traversed
        roots_p = traverse(root, p)
        roots_q = traverse(root, q)
        print([n.val for n in roots_p], [m.val for m in roots_q])
        for n in roots_p[::-1]:
            for m in roots_q[::-1]:
                if m is n:
                    return m

class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ My own solution. 类似back tracking 回溯，recursive，dfs. similar to https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-26/ 
        master theorem o(n)
        """
        def dfs(root, node, path):
            if not root:
                return False
            if root.val == node.val:
                path.append(root)
                return True
            path.append(root)
            if dfs(root.left, node, path) or dfs(root.right, node, path):
                return True
            path.pop()
        path_p = []
        dfs(root, p, path_p)
        # print([node.val for node in path_p])
        path_q = []
        dfs(root, q, path_q)
        # print([node.val for node in path_q])
        lca = root
        for node_p, node_q in zip(path_p, path_q):
            if node_p is node_q:
                lca = node_p
            else:
                break
        return lca

class Solution2:
    ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ 这个解其实更好理解
        dfs 后序遍历 https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/er-cha-shu-de-zui-jin-gong-gong-zu-xian-by-leetc-2/ 解释，注意把任何提到 子树中是否包含 p 节点或 q 节点 ，替换为 以root 为根结点的树是否包含p 节点或q节点
        时间复杂度：O(N)O(N)，其中 NN 是二叉树的节点数。二叉树的所有节点有且只会被访问一次，因此时间复杂度为 O(N)O(N)。

        空间复杂度：O(N)O(N) ，其中 NN 是二叉树的节点数。递归调用的栈深度取决于二叉树的高度，二叉树最坏情况下为一条链，此时高度为 NN，因此空间复杂度为 O(N)O(N)。

        """
        def dfs(root, p, q):
            # 以root 为 根结点 的树是否包含p 或 q
            if not root:
                return False
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            if (left and right) or ((root is p or root is q) and (left or right)):
                # root 是 最近公共祖先条件
                self.ans = root
            # 以root 为 根结点 的树是否包含p 或 q
            return left or right or root is p or root is q
        dfs(root, p, q)
        return self.ans


class Solution3:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ postorder traverse/DFS  这个解可能不好理解
        看解释https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/zui-jin-gong-gong-zu-xian-tong-guo-yan-shen-ding-y/
        图：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/
        """
        if not root or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root
