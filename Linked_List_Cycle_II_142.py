

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution2:
    """ https://leetcode-cn.com/leetbook/read/linked-list/jjhf6/ """
    def detectCycle(self, head: ListNode) -> ListNode:
        """ ref: https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/
        """
        # latest try
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        if not fast or not fast.next:
            return
        new_pointer = head
        while new_pointer is not slow:
            slow = slow.next
            new_pointer = new_pointer.next
        return slow

        if head is None:
            return None
        fast_pointer = slow_pointer = head
        while True:
            fast_pointer = fast_pointer.next
            if fast_pointer is None:
                return None
            fast_pointer = fast_pointer.next
            if fast_pointer is None:
                return None
            slow_pointer = slow_pointer.next
            if slow_pointer is None:
                return None
            if fast_pointer is slow_pointer:
                # met the first time
                break
        # one pointer restart from head
        fast_pointer = head
        while True:
            # met the second time
            if fast_pointer is slow_pointer:
                return slow_pointer
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next

    def detectCycle2(self, head: ListNode) -> ListNode:
        """ https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/huan-xing-lian-biao-ii-by-leetcode-solution/ """
        node_seen = set()
        pointer = head
        while pointer is not None:
            if pointer not in node_seen:
                node_seen.add(pointer)
            else:
                # the first time seen already, is the node enter the circle
                return pointer
            pointer = pointer.next
        return None
