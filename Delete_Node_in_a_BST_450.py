# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """ my own solution. iterative solution. 两种方法
        时间复杂度：\mathcal{O}(\log N)O(logN)。
        空间复杂度：O(1)
        思路：https://leetcode-cn.com/leetbook/read/introduction-to-data-structure-binary-search-tree/xpyd7r/
        """
        if not root:
            return
        pre = TreeNode()
        pre.left = node = root
        dumb = pre
        left = True
        while node:
            if key == node.val:
                if not node.left and not node.right:
                    if left:
                        pre.left = None
                    else:
                        pre.right = None
                elif not node.left:
                    if left:
                        pre.left = node.right
                    else:
                        pre.right = node.right
                elif not node.right:
                    if left:
                        pre.left = node.left
                    else:
                        pre.right = node.left
                else:
                    # method 1: 
                    '''
                    if left:
                        pre.left = node.left
                    else:
                        pre.right = node.left
                    pointer = node.left
                    while pointer.right:
                        pointer = pointer.right
                    pointer.right = node.right
                    node.left = node.right = None
                    '''
                    # method 2
                    pre_p = pointer = node.right
                    while pointer.left:
                        pre_p = pointer
                        pointer = pointer.left
                    pre_p.left = None
                    if left:
                        pre.left = pointer
                    else:
                        pre.right = pointer
                    pointer.left = node.left
                    new_pointer = pointer
                    while new_pointer.right:
                        new_pointer = new_pointer.right
                    if pointer != node.right:
                        new_pointer.right = node.right
                    node.left = node.right = None
                return dumb.left
            elif key < node.val:
                pre = node
                left = True
                node = node.left
            else:
                left = False
                pre = node
                node = node.right
        return dumb.left


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def successor(self, node):
        if not node:
            return
        pointer = node.right
        while pointer.left:
            pointer = pointer.left
        return pointer

    def predecessor(self, node):
        if not node:
            return
        pointer = node.left
        while pointer.right:
            pointer = pointer.right
        return pointer

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """ bst recursive不改值的解: https://leetcode-cn.com/problems/delete-node-in-a-bst/solution/shan-chu-er-cha-sou-suo-shu-zhong-de-jie-dian-by-l/ Yaokunwu 回复Joy
        时间复杂度：\mathcal{O}(\log N)O(logN)。根据master theorem
        空间复杂度：\mathcal{O}(H)O(H)，递归时堆栈使用的空间，HH 是树的高度。

        """
        if not root:
            return
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                # root = None
                return
            elif root.right:
                suc = self.successor(root)
                print(suc)
                suc.right = self.deleteNode(root.right, suc.val)
                suc.left = root.left
                # root.left = root.right = None
                return suc
            else:
                pred = self.predecessor(root)
                pred.left = self.deleteNode(root.left, pred.val)
                # root.left = root.right = None
                return pred
        return root


class Solution2:
    """ 思路similar to https://leetcode-cn.com/problems/delete-node-in-a-bst/solution/yong-qian-qu-huo-zhe-hou-ji-jie-dian-zi-shu-dai-ti/ """
    def get_predecessor_node(self, root):
        if root.left:
            node = root.left
            pre = node
            while node.right:
                pre = node
                node = node.right
            pre.right = node.left
            return node
        return root
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        elif root.val == key:
            predecessor_node = self.get_predecessor_node(root)
            if predecessor_node is root:
                return root.right
            if root.left is not predecessor_node:
                predecessor_node.left = root.left
            predecessor_node.right = root.right
            root.left = None
            root.right = None
            return predecessor_node
        elif root.val > key:
            left_root = self.deleteNode(root.left, key)
            root.left = left_root
            return root
        else:
            right_root = self.deleteNode(root.right, key)
            root.right = right_root
            return root

class Solution3:
    """ 最简单的解法，https://leetcode-cn.com/problems/delete-node-in-a-bst/solution/miao-dong-jiu-wan-shi-liao-by-terry2020-tc0o/
    会增加树的高度
    """
    def get_predecessor_node(self, root):
        if root.left:
            node = root.left
            while node.right:
                node = node.right
            return node
        return root
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        elif root.val == key:
            if not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                predecessor_node = self.get_predecessor_node(root)
                predecessor_node.right = root.right
                root = root.left
        elif root.val > key:
            left_root = self.deleteNode(root.left, key)
            root.left = left_root
        else:
            right_root = self.deleteNode(root.right, key)
            root.right = right_root
        return root
