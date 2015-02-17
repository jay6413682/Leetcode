# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, nxt=None):
        self.val = x
        self.next = nxt


class Solution1:
    def isPalindrome(self, head: ListNode) -> bool:
        """ 双指针，快慢指针，链表反转 similar to https://leetcode-cn.com/problems/palindrome-linked-list/solution/wo-de-kuai-man-zhi-zhen-du-cong-tou-kai-shi-gan-ju/
        杨昆 comment
        time: O(n), space: O(1)
        """
        if not head:
            return
        slow = head
        fast = head
        curr = head
        nxt = curr.next
        prev = None
        # 快慢指针，并同时反转链表前半部分
        while fast and fast.next:
            # print(slow.val, fast.val)
            curr = slow
            fast = fast.next.next
            slow = slow.next
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = curr.next
        # print(slow.val, fast, prev.val, curr.val, nxt.val)
        if fast:
            right_head = nxt
            left_head = prev
        else:
            if prev.val != curr.val:
                return False
            right_head = nxt
            left_head = prev.next
        # 比较值
        while left_head:
            if left_head.val != right_head.val:
                return False
            left_head = left_head.next
            right_head = right_head.next
        return True


class Solution:
    def reverse_linked_list(self, head: ListNode) -> ListNode:
        pointer = head
        while pointer is not None and pointer.next is not None:
            nxt = pointer.next
            nxt_nxt = pointer.next.next
            nxt.next = head
            head = nxt
            pointer.next = nxt_nxt
        return head

    def isPalindrome(self, head: ListNode) -> bool:
        """ https://leetcode-cn.com/problems/palindrome-linked-list/solution/hui-wen-lian-biao-by-leetcode-solution/ """
        # 找到前半部分链表的尾节点。
        dummpy_node = ListNode(None)
        dummpy_node.next = head
        slow_pointer = dummpy_node
        fast_pointer = dummpy_node
        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        # reverse right half linked list
        right_half_head = slow_pointer.next
        reversed_right_half_head = self.reverse_linked_list(right_half_head)
        # 判断是否回文。
        right_pointer = reversed_right_half_head
        left_pointer = head
        while right_pointer is not None:
            if left_pointer.val != right_pointer.val:
                # reverse back right half linked list
                slow_pointer.next = right_half_head = self.reverse_linked_list(reversed_right_half_head)
                return False
            right_pointer = right_pointer.next
            left_pointer = left_pointer.next
        # reverse back right half linked list
        slow_pointer.next = right_half_head = self.reverse_linked_list(reversed_right_half_head)
        return True

    def isPalindrome2(self, head: ListNode) -> bool:
        """ https://leetcode-cn.com/problems/palindrome-linked-list/solution/hui-wen-lian-biao-by-leetcode-solution/
        时间复杂度：O(n)O(n)
        空间复杂度：O(n)O(n)
        """
        lst = []
        while head is not None:
            lst.append(head.val)
            head = head.next
        return lst == lst[::-1]


class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        """ This solution (my own) has o(1) space but o(n^2) time complexity; it timesout """
        if not head:
            return
        counter = 0
        pointer = head
        while pointer:
            counter += 1
            pointer = pointer.next
        steps = 0
        while steps <= counter - 1 - steps:
            # steps = 0, counter - steps - 1 = 4
            pointer = head
            # print(steps)
            temp = steps
            while temp > 0:
                pointer = pointer.next
                temp -= 1
            val_a = pointer.val
            temp = counter - steps * 2 - 1
            while temp > 0:
                pointer = pointer.next
                temp -= 1
            val_b = pointer.val
            if val_a != val_b:
                return False
            steps += 1
        return True
