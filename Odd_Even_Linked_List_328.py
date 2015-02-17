# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """ https://leetcode-cn.com/problems/odd-even-linked-list/solution/qi-ou-lian-biao-by-leetcode-solution/ """
        if head is None:
            return head
        odd_pointer = head
        even_pointer = even_head = head.next
        while even_pointer is not None:
            third_pointer = even_pointer.next
            if third_pointer is None:
                even_pointer.next = None
            else:
                even_pointer.next = third_pointer.next
            odd_pointer.next = third_pointer
            even_pointer = even_pointer.next
            if odd_pointer.next is not None:
                odd_pointer = odd_pointer.next

        odd_pointer.next = even_head
        return head
        """
        # my second try
        if not head:
            return
        if not head.next:
            return head
        h1 = p1 = head
        h2 = p2 = head.next
        while p1.next and p2.next:
            p1.next = p2.next
            p1 = p1.next
            p2.next = p2.next.next
            p2 = p2.next
        p1.next = h2
        return h1
        """

    def oddEvenList2(self, head: ListNode) -> ListNode:
        """ https://leetcode-cn.com/problems/odd-even-linked-list/solution/kuai-lai-wu-nao-miao-dong-qi-ou-lian-biao-by-sweet/ """
        odd_head = ListNode()
        odd_tail = odd_head
        even_head = ListNode()
        even_tail = even_head
        pointer = head
        is_odd = True
        while pointer is not None:
            if is_odd:
                odd_tail.next = pointer
                odd_tail = pointer
            else:
                even_tail.next = pointer
                even_tail = pointer
            pointer = pointer.next
            is_odd = not is_odd
        odd_tail.next = even_head.next
        even_tail.next = None
        return odd_head.next
