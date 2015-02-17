

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """ https://leetcode-cn.com/leetbook/read/linked-list/jbex5/
        https://leetcode-cn.com/problems/linked-list-cycle/solution/ckuai-man-zhi-zhen-dai-zhu-shi-by-xi-yu-shi-liu-gu/ (ljjTYJR):
        关于快慢指针中两个指针的速度问题： 和龟兔赛跑问题不同的是，龟兔赛跑是一个连续性的问题，无论二者的速度差是多少，可以这样假设：假设赛道长度为s，v_f表示速度快的值，v_s表示速度慢的值，（假设二者初始位置相同），那么可以求出来：(v_f-v_s)t=s；这样求出来的t，是二者第一次相遇的时间； 本题不同的是：对于链表来说是一个离散的值，我们假设环内共有n个节点，同样假设快指针与慢指针分别是v_f，v_s；如果想要相遇（假设初始位置相同），同样有(v_f-v_s)k = n； ——这个时候 v_f，v_s 为正整数，k为循环次数，n为节点数目； k = n/(v_f-v_s）如果想要k为整数，那么可以看到二者的速度差是有要求的，必须能够被n整除；注意：这样求得是第一次相遇，也有可能v_f-v_s是n的整数倍；
        """
        if head is None:
            return False
        fast_pointer = slow_pointer = head
        while True:
            fast_pointer = fast_pointer.next
            if fast_pointer is None:
                return False
            fast_pointer = fast_pointer.next
            if fast_pointer is None:
                return False
            slow_pointer = slow_pointer.next
            if slow_pointer is None:
                return False
            if fast_pointer is slow_pointer:
                return True
        '''
        # try number 2
        if not head:
            return False
        if not head.next:
            return False
        dummy = ListNode()
        dummy.next = head
        pointer_a = dummy
        pointer_b = dummy
        while pointer_a and pointer_b:
            pointer_a = pointer_a.next
            pointer_b = pointer_b.next
            if pointer_b:
                pointer_b = pointer_b.next
            else:
                return False
            if pointer_a is pointer_b:
                return True
        '''
