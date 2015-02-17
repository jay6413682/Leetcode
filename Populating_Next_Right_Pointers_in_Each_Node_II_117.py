"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """ 层序遍历，与116解法相同：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/solution/tian-chong-mei-ge-jie-dian-de-xia-yi-ge-you-ce-15/
        记树上的点的个数为 NN。

        时间复杂度：O(N)O(N)。我们需要遍历这棵树上所有的点，时间复杂度为 O(N)O(N)。

        空间复杂度：O(N)O(N)。即队列的空间代价。
        """
        if not root:
            return root
        queue = [root]
        while queue:
            i = 0
            n = len(queue)
            while i < n:
                node = queue.pop(0)
                if i < n - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                i += 1
        return root
        """
        # second try
        if not root:
            return
        queue = deque([root])
        while queue:
            n = len(queue)
            # print([i.val for i in queue])
            for i in range(n):
                node = queue.popleft()
                # print(node.val, [i.val for i in queue])
                if i < n - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
        """


class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        """ 
        bfs + linked list:
        https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/solution/bfsjie-jue-zui-hao-de-ji-bai-liao-100de-yong-hu-by/
        O(1) space complexity
        """
        """
        # second try
        if not root:
            return
        curr_level_node = root
        while curr_level_node:
            dummy = Node()
            next_level_node = dummy
            while curr_level_node:
                if curr_level_node.left:
                    next_level_node.next = curr_level_node.left
                    next_level_node = next_level_node.next
                if curr_level_node.right:
                    next_level_node.next = curr_level_node.right
                    next_level_node = next_level_node.next
                curr_level_node = curr_level_node.next
            curr_level_node = dummy.next
        return root
        """
        if not root:
            return root
        curr = root
        while curr:
            dummy = Node()
            pre = dummy
            while curr:
                if curr.left:
                    pre.next = curr.left
                    pre = pre.next
                if curr.right:
                    pre.next = curr.right
                    pre = pre.next
                curr = curr.next
            curr = dummy.next
        return root
