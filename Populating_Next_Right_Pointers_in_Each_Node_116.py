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
        """ 层序遍历：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/solution/tian-chong-mei-ge-jie-dian-de-xia-yi-ge-you-ce-2-4/
        复杂度分析

        时间复杂度：O(N)O(N)。每个节点会被访问一次且只会被访问一次，即从队列中弹出，并建立 \text{next}next 指针。

        空间复杂度：O(N)O(N)。这是一棵完美二叉树，它的最后一个层级包含 N/2个节点。广度优先遍历的复杂度取决于一个层级上的最大元素数量。这种情况下空间复杂度为 O(N)O(N)。
        为什么它的最后一个层级包含 N/2个节点：
        https://en.wikipedia.org/wiki/1/2_%2B_1/4_%2B_1/8_%2B_1/16_%2B_%E2%8B%AF#cite_note-1
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
                # or:
                # if queue and i > 0:
                #    queue[-1].next = node.left
                if node.left:
                    queue.append(node.left)
                    # node.left.next = node.right
                if node.right:
                    queue.append(node.right)
                i += 1
        return root
        """
        # my second try:
        if not root:
            return
        queue = deque([root])
        while queue:
            i = 0
            n = len(queue)
            pre = queue.popleft()
            if pre.left and pre.right:
                queue.extend([pre.left, pre.right])
            while i < n - 1:
                after = queue.popleft()
                if after.left and after.right:
                    queue.extend([after.left, after.right])
                pre.next = after
                pre = pre.next
                i += 1
            # print([n.val for n in queue])
        return root
        """


class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        """ https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/solution/tian-chong-mei-ge-jie-dian-de-xia-yi-ge-you-ce-2-4/
        时间复杂度：O(N)O(N)，每个节点只访问一次。

        空间复杂度：O(1)O(1)，不需要存储额外的节点。    
        """
        if not root:
            return root
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root
        """
        # second try
        if not root:
            return
        node = root
        while node.left:
            leftmost_node = node
            while node:
                right_child = node.right
                left_child = node.left
                left_child.next = right_child
                node = node.next
                if not node:
                    break
                right_child.next = node.left

            node = leftmost_node.left
        return root
        """


class Solution3:
    def connect(self, root: 'Node') -> 'Node':
        """ dfs, recursive，递归：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/solution/dong-hua-yan-shi-san-chong-shi-xian-116-tian-chong/
        时间复杂度：O(n)O(n)
        空间复杂度：O(h)O(h)，hh 是树的高度
        """
        if not root:
            return root
        left = root.left
        right = root.right
        while left:
            left.next = right
            left = left.right
            right = right.left
        self.connect(root.left)
        self.connect(root.right)
        return root
