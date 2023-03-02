# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """ https://leetcode-cn.com/problems/intersection-of-two-linked-lists/ """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """ 哈希表法: https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/xiang-jiao-lian-biao-by-leetcode/ """
        pointer_a = headA
        pointer_b = headB
        seen = set()
        while pointer_a is not None:
            seen.add(pointer_a)
            pointer_a = pointer_a.next
        while pointer_b is not None:
            if pointer_b in seen:
                return pointer_b
            pointer_b = pointer_b.next
        return None

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        """ 解：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/python-san-chong-jie-fa-fu-tu-xiang-jie-by-da_bo_l
        方法3初看很难理解，但是细想就会发现很简单很巧妙 A和B两个链表长度可能不同，但是A+B和B+A的长度是相同的，所以遍历A+B和遍历B+A一定是同时结束。 如果A,B相交的话A和B有一段尾巴是相同的，所以两个遍历的指针一定会同时到达交点 如果A,B不相交的话两个指针就会同时到达A+B（B+A）的尾节点
        证明：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/xiang-jiao-lian-biao-by-leetcode-solutio-a8jn/
        图例：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/tu-jie-xiang-jiao-lian-biao-by-user7208t/
        """
        pointer_a = headA
        pointer_b = headB
        if pointer_a is None or pointer_b is None:
            return None
        while pointer_a is not pointer_b:
            if pointer_a is None:
                pointer_a = headB
            else:
                pointer_a = pointer_a.next
            if pointer_b is None:
                pointer_b = headA
            else:
                pointer_b = pointer_b.next
        return pointer_b

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """ 快慢指针 linked list my solution """
        slow = fast = headA
        fast_pre = ListNode(-1)
        fast_pre.next = fast
        met_none = False
        tail = None
        # 快慢指针从 其中一个head 往前走 fast先到null 与另一个头节点相连，问题转化为 Linked List Cycle  问题
        while True:
            if fast and fast.next:
                fast_pre = fast_pre.next.next
                fast = fast.next.next
            else:
                if met_none:
                    # 注意reset tail 与 head之间的连接
                    tail.next = None
                    return None
                if fast:
                    tail = fast
                    fast.next = headB
                    fast = fast.next.next
                    fast_pre = fast_pre.next.next
                else:
                    tail = fast_pre
                    fast_pre.next = headB
                    fast = headB
                    fast = fast.next.next
                    fast_pre = fast_pre.next.next
                met_none = True
            if slow:
                slow = slow.next
            else:
                return None
            if slow is fast:
                break

        #print('slow: ', slow, '\n', 'fast: ', fast)
        new_pointer = headA
        while new_pointer is not slow:
            new_pointer = new_pointer.next
            slow = slow.next
        # 注意reset tail 与 head之间的连接
        tail.next = None
        return slow


class Solution3:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """ My solution, needs visited attribute on the node
        """
        node = headA
        while node:
            node.visited = True
            node = node.next
        node = headB
        while node:
            if hasattr(node, 'visited') and node.visited is True:
                return node
            node = node.next
        return
