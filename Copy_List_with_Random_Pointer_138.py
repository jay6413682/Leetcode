

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution1:
    visited = {}
    def copyRandomList(self, head: 'Node') -> 'Node':
        # dfs solution, 类似 https://leetcode-cn.com/problems/copy-list-with-random-pointer/solution/python3-shen-du-sou-suo-by-ting-ting-28/
        if not head:
            return
        if head in self.visited:
            return self.visited[head]
        copied_head = Node(head.val)
        self.visited[head] = copied_head
        copied_head.next = self.copyRandomList(head.next)
        copied_head.random = self.copyRandomList(head.random)
        return copied_head


class Solution:
    """ This is my own solution. Not finding any others with same solution
    https://leetcode-cn.com/leetbook/read/linked-list/fdi26/
    """
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        pointer = head
        # save mapping between node and random
        node_random_mapping = {}
        node_list = []
        node_copy_list = []
        while pointer is not None:
            node_random_mapping[pointer] = pointer.random
            node_list.append(pointer)
            nxt = pointer.next
            # firstly clone the nodes without random link
            if not node_copy_list:
                # the first iteration, create the first node
                node_copy = Node(pointer.val)
            if nxt:
                node_copy.next = Node(nxt.val)
            node_copy_list.append(node_copy)
            pointer = pointer.next
            node_copy = node_copy.next
        # clone the randoms link
        for i, node in enumerate(node_list):
            random = node_random_mapping[node]
            if random:
                node_copy = node_copy_list[i]
                original_random_i = node_list.index(random)
                random_copy = node_copy_list[original_random_i]
                node_copy.random = random_copy

        return node_copy_list[0]


class Solution2:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """ https://leetcode-cn.com/problems/copy-list-with-random-pointer/solution/liang-chong-shi-xian-tu-jie-138-fu-zhi-dai-sui-ji-/ """
        if not head:
            return head
        pointer = head
        # 创建一个哈希表，key是原节点，value是新节点    
        node_clone_map = {}
        # 将原节点和新节点放入哈希表中
        while pointer is not None:
            node_clone_map[pointer] = Node(pointer.val)
            pointer = pointer.next
        pointer = head
        # 遍历原链表，设置新节点的next和random
        while pointer is not None:
            # p是原节点，d[p]是对应的新节点，p.next是原节点的下一个
            # d[p.next]是原节点下一个对应的新节点
            if pointer.next:
                node_clone_map[pointer].next = node_clone_map[pointer.next]
            # p.random是原节点随机指向
            # d[p.random]是原节点随机指向  对应的新节点    
            if pointer.random:
                node_clone_map[pointer].random = node_clone_map[pointer.random]
            pointer = pointer.next
        # 返回头结点，即原节点对应的value(新节点)
        return node_clone_map[head]


class Solution3(object):
    def copyRandomList(self, head: 'Node') -> 'Node':
        """ https://leetcode-cn.com/problems/copy-list-with-random-pointer/solution/liang-chong-shi-xian-tu-jie-138-fu-zhi-dai-sui-ji-/ and https://leetcode-cn.com/problems/copy-list-with-random-pointer/solution/fu-zhi-dai-sui-ji-zhi-zhen-de-lian-biao-by-leetcod/ """
        if not head:
            return head
        pointer = head
        # Creating a new weaved list of original and copied nodes.
        while pointer is not None:
            # Cloned node
            pointer_copy = Node(pointer.val)
            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            pointer_copy.next = pointer.next
            pointer.next = pointer_copy
            pointer = pointer_copy.next
        pointer = head
        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes.
        while pointer is not None:
            pointer.next.random = pointer.random.next if pointer.random else None
            pointer = pointer.next.next
        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        pointer = head
        dummpy_head = Node(-1, head)
        pointer_copy = dummpy_head
        while pointer is not None:
            pointer_copy.next = pointer.next
            pointer_copy = pointer_copy.next
            pointer.next = pointer_copy.next
            pointer = pointer.next

        return dummpy_head.next
