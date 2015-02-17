# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
在对链表进行操作时，一种常用的技巧是添加一个哑节点（dummy node），它的 \textit{next}next 指针指向链表的头节点。这样一来，我们就不需要对头节点进行特殊的判断了。

例如，在本题中，如果我们要删除节点 yy，我们需要知道节点 yy 的前驱节点 xx，并将 xx 的指针指向 yy 的后继节点。但由于头节点不存在前驱节点，因此我们需要在删除头节点时进行特殊判断。但如果我们添加了哑节点，那么头节点的前驱节点就是哑节点本身，此时我们就只需要考虑通用的情况即可。
'''


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """ If list is allowed, my solution """
        node_list = []
        i = 0
        pointer = head
        while pointer is not None:
            node_list.append(pointer)
            pointer = pointer.next
            i += 1
        i -= 1
        if i - n < 0:
            # delete the first node
            return head.next
        node_list[i - n].next = node_list[i - n].next.next
        return head

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        """ 双指针：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/solution/dong-hua-tu-jie-leetcode-di-19-hao-wen-ti-shan-chu/ """
        dummy_head = ListNode(next=head)
        first_pointer = dummy_head
        second_pointer = dummy_head
        i = 0
        while i <= n:
            second_pointer = second_pointer.next
            i += 1
        while second_pointer is not None:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next
        first_pointer.next = first_pointer.next.next
        return dummy_head.next

    def removeNthFromEnd3(self, head: ListNode, n: int) -> ListNode:
        """ 如果允许栈（list）https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/solution/shan-chu-lian-biao-de-dao-shu-di-nge-jie-dian-b-61/
        时间复杂度：O(L)O(L)，其中 LL 是链表的长度。

        空间复杂度：O(L)O(L)，其中 LL 是链表的长度。主要为栈的开销。
        """
        dummy_head = ListNode(next=head)
        node_stack = []
        pointer = dummy_head
        while pointer is not None:
            node_stack.append(pointer)
            pointer = pointer.next
        i = 0
        while i < n:
            node_stack.pop()
            i += 1

        prev = node_stack[-1]
        prev.next = prev.next.next
        return dummy_head.next
