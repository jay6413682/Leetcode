# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """ https://leetcode-cn.com/problems/remove-linked-list-elements/solution/yi-chu-lian-biao-yuan-su-by-leetcode/
        双指針 + dummy head
        """
        dummpy_node = ListNode(None)
        dummpy_node.next = head
        prev = dummpy_node
        curr = head
        while curr is not None:
            nxt = curr.next
            if curr.val == val:
                prev.next = nxt
                curr.next = None
            else:
                prev = prev.next
            curr = nxt
        return dummpy_node.next
