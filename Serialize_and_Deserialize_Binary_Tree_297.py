# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec3:
    """ My own bfs solution after optimization; similar to https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/solution/shou-hui-tu-jie-gei-chu-dfshe-bfsliang-chong-jie-f/
    复杂度分析

    时间复杂度：O(n)
    空间复杂度：O(n)
    """

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return []
        queue = [root]
        while queue:
            n = len(queue)
            i = 0
            while i < n:
                node = queue.pop(0)
                if node:
                    node_val = node.val
                    res.append(str(node_val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    res.append('N')
                i += 1
        return ','.join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        l = data.split(',')
        # not use pop but move cursor
        # root = TreeNode(int(l.pop(0)))
        root = TreeNode(int(l[0]))
        queue = [root]
        i = 1
        while queue:
            # n = len(queue)
            # i = 0
            # 不需要层序遍历
            # while i < n:
            node = queue.pop(0)
            # node val cannot be None
            node_val = node.val
            # not use pop but move cursor; this makes it more efficient
            # left_val = l.pop(0)
            left_val = l[i]
            # right_val = l.pop(0)
            right_val = l[i + 1]
            if left_val != 'N':
                left = TreeNode(int(left_val))
                queue.append(left)
                node.left = left
            if right_val != 'N':
                right = TreeNode(right_val)
                queue.append(right)
                node.right = right
                # i += 1
            i += 2
        return root
    '''
    # try no. 2
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        # print(root)
        if not root:
            return 'null'
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                node_val = node.val
                res.append(node_val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append(None)
        # print(json.dumps(res))
        return json.dumps(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # print(data)
        data = json.loads(data)
        if not data:
            return
        n = len(data)
        i = 1
        root = TreeNode(data[0])
        parents = deque([root])
        while i < n:
            # print(i, parents)
            node = parents.popleft()
            left_val = data[i]
            right_val = data[i + 1]
            if left_val is not None:
                # must be is not None, to avoid case of left_val is 0
                node.left = TreeNode(left_val)
                parents.append(node.left)
            if right_val is not None:
                node.right = TreeNode(right_val)
                parents.append(node.right)
            i += 2
        return root
    '''


class Codec:
    """ My own bfs solution; not efficient"""

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return []
        queue = [root]
        while queue:
            n = len(queue)
            i = 0
            while i < n:
                node = queue.pop(0)
                if node:
                    node_val = node.val
                    res.append(str(node_val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    res.append('N')
                i += 1
        return ','.join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        l = data.split(',')
        root = TreeNode(int(l.pop(0)))
        queue = [root]
        while queue:
            n = len(queue)
            i = 0
            while i < n:
                node = queue.pop(0)
                if node:
                    node_val = node.val
                    if str(node_val).lstrip('-').isdigit():
                        left_val = l.pop(0)
                        right_val = l.pop(0)
                        if left_val.lstrip('-').isdigit():
                            left = TreeNode(int(left_val))
                        else:
                            left = None
                        if right_val.lstrip('-').isdigit():
                            right = TreeNode(right_val)
                        else:
                            right = None
                        queue.append(left)
                        queue.append(right)
                        node.left = left
                        node.right = right
                i += 1
        return root
            

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


class Codec2:
    """ dfs / preorder traversal / 选择前序遍历，是因为 根|左|右根∣左∣右 的打印顺序，在反序列化时更容易定位出根节点的值。
    https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/solution/shou-hui-tu-jie-gei-chu-dfshe-bfsliang-chong-jie-f/
    复杂度：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/solution/er-cha-shu-de-xu-lie-hua-yu-fan-xu-lie-hua-by-le-2/
    时间复杂度：在序列化和反序列化函数中，我们只访问每个节点一次，因此时间复杂度为 O(n)O(n)，其中 nn 是节点数，即树的大小。
    空间复杂度：在序列化和反序列化函数中，我们递归会使用栈空间，故渐进空间复杂度为 O(n)O(n)。

    """

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'N'
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + ',' + left + ',' + right


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def build_tree(l):
            root_val = l.pop(0)
            if root_val == 'N':
                return None
            root = TreeNode(root_val)
            root.left = build_tree(l)
            root.right = build_tree(l)
            return root
        return build_tree(data.split(','))
        
            

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
