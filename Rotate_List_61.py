# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """ My own solution: time complexity O(N), space complexity O(N) """
        if not head:
            return head
        l_node = []
        pointer = head
        while pointer is not None:
            l_node.append(pointer)
            pointer = pointer.next
        node_size = len(l_node)
        k = k % node_size
        while k > 0:
            l_node.insert(0, l_node[-1])
            l_node.pop()
            l_node[-1].next = None
            if node_size > 1:
                l_node[0].next = l_node[1]
            k -= 1
        return l_node[0]


class Solution2:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """ https://leetcode-cn.com/problems/rotate-list/solution/xuan-zhuan-lian-biao-by-leetcode-solutio-woq1/
        时间复杂度：O(n)O(n)，最坏情况下，我们需要遍历该链表两次。

        空间复杂度：O(1)O(1)，我们只需要常数的空间存储若干变量。
        """
        """
        if not head:
            return head
        if not head.next:
            return head
        pointer = head
        counter = 1
        while pointer.next is not None:
            pointer = pointer.next
            counter += 1
        m = counter - k % counter
        pointer.next = head
        while m > 0:
            m -= 1
            pointer = pointer.next
        new_head = pointer.next
        pointer.next = None
        return new_head
        """

        if not head:
            return None
        steps = 0
        dummpy = ListNode(next=head)
        pointer = dummpy
        while pointer.next:
            steps += 1
            pointer = pointer.next
        pointer.next = head
        # print(steps, k)
        if steps == k:
            extra_steps = 0
        else:
            extra_steps = steps - k % steps
        while extra_steps > 0:
            pointer = pointer.next
            extra_steps -= 1
        new_head = pointer.next
        pointer.next = None
        return new_head
