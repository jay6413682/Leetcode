# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """ https://leetcode-cn.com/leetbook/read/linked-list/fx61e/
        or https://leetcode-cn.com/problems/reverse-linked-list/solution/fan-zhuan-lian-biao-shuang-zhi-zhen-di-gui-yao-mo-/
        妖魔化的双指针
        """
        pointer = head
        if pointer is None:
            return None
        while pointer.next is not None:
            nxt = pointer.next
            nxt_nxt = pointer.next.next
            nxt.next = head
            head = nxt
            pointer.next = nxt_nxt
        return head
        """
        # my solution, very similar, easier to understand. 画图，curr就是要reverse next 指针的new head
        # 解法其实就是根据图，判断都需要存储哪几个节点：original head，new head（变化中），dummy 的next
        if not head:
            return head
        dummy = ListNode(next=head)
        curr = head.next
        while curr:
            nxt = curr.next
            curr.next = dummy.next
            dummy.next = curr
            curr = nxt
            head.next = curr
        return dummy.next
        """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        """ 简单双指针迭代：https://leetcode-cn.com/problems/reverse-linked-list/solution/fan-zhuan-lian-biao-shuang-zhi-zhen-di-gui-yao-mo-/ """
        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution3:
    def reverseList(self, head: ListNode) -> ListNode:
        """ 递归的模板：https://leetcode-cn.com/problems/reverse-linked-list/solution/3chong-jie-jue-fang-shi-zhan-shuang-lian-biao-di-2/ """
        # 中止条件
        if head is None or head.next is None: 
            return head

        # 逻辑处理（可能有，也可能没有，具体问题具体分析）
        nxt = head.next
        # 递归调用
        reverse_head = self.reverseList(nxt);

        # 逻辑处理（可能有，也可能没有，具体问题具体分析）
        nxt.next = head
        head.next = None
        return reverse_head
        """
        # tail recursion
        def reverse_list(pre, curr):
            if not curr:
                return pre
            nxt = curr.next
            curr.next = pre
            return reverse_list(curr, nxt)
        return reverse_list(None, head)
        """

