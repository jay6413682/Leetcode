# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """ 顺序合并: https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/he-bing-kge-pai-xu-lian-biao-by-leetcode-solutio-2/ """
    def merge_two_lists(self, node_a: ListNode, node_b: ListNode) -> ListNode:
        if not node_a:
            return node_b
        if not node_b:
            return node_a
        merged_dummy_head = ListNode()
        merged_pointer = merged_dummy_head
        pointer_a = node_a
        pointer_b = node_b
        while pointer_a is not None and pointer_b is not None:
            if pointer_a.val < pointer_b.val:
                merged_pointer.next = pointer_a
                pointer_a = pointer_a.next
            else:
                merged_pointer.next = pointer_b
                pointer_b = pointer_b.next
            merged_pointer = merged_pointer.next
        if pointer_a is not None:
            merged_pointer.next = pointer_a
        elif pointer_b is not None:
            merged_pointer.next = pointer_b
        return merged_dummy_head.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        m = None
        for l in lists:
            m = self.merge_two_lists(m, l)
        return m


class Solution2:
    """ My own solution, not efficient """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        merged_list_dummpy_head = ListNode(-10**4 - 1)

        for l in lists:
            if not l:
                continue
            pointer = l
            while pointer is not None:
                merged_list_pointer_slow = merged_list_dummpy_head
                merged_list_pointer_fast = merged_list_pointer_slow.next
                nxt = pointer.next
                while merged_list_pointer_slow is not None:
                    if (merged_list_pointer_fast is not None and pointer.val >= merged_list_pointer_slow.val and pointer.val <= merged_list_pointer_fast.val) or (merged_list_pointer_fast is None):
                        pointer.next = merged_list_pointer_fast
                        merged_list_pointer_slow.next = pointer
                        break
                    merged_list_pointer_slow = merged_list_pointer_slow.next
                    if merged_list_pointer_fast is not None:
                        merged_list_pointer_fast = merged_list_pointer_fast.next
                pointer = nxt
        return merged_list_dummpy_head.next


class Solution3:
    """ 堆/优先序列；use heapq : to represent priority queue: https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/ 
    working solution: https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/python-c-you-xian-dui-lie-zui-xiao-dui-onlogk-by-m/
    not working in python 3: https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/duo-tu-yan-shi-23-he-bing-kge-pai-xu-lian-biao-by-/
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        n = len(lists)
        if n == 1:
            return lists[0]
        import heapq
        q = []
        dummpy_head = ListNode(-1)
        merged_pointer = dummpy_head
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(q, (l.val, i))
        while q:
            val, i = heapq.heappop(q)
            # why cannot i use pointer = lists[i] here????
            # because the next node needs to be saved to the lists; so in one of next loops, we can access it.
            merged_pointer.next = lists[i]
            merged_pointer = merged_pointer.next
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(q, (lists[i].val, i))
        return dummpy_head.next


class Solution4:
    """
    归并/merge 法： https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/he-bing-kge-pai-xu-lian-biao-by-leetcode-solutio-2/
    归并排序最好的解释： https://zhuanlan.zhihu.com/p/44656243
    归并排序复杂度解析：https://blog.csdn.net/YuZhiHui_No1/article/details/44223225 (也可用master theorem)
    https://zhuanlan.zhihu.com/p/124356219
    
    """
    def merge_two_lists(self, node_a: ListNode, node_b: ListNode) -> ListNode:
        if not node_a:
            return node_b
        if not node_b:
            return node_a
        merged_dummy_head = ListNode()
        merged_pointer = merged_dummy_head
        pointer_a = node_a
        pointer_b = node_b
        while pointer_a is not None and pointer_b is not None:
            if pointer_a.val < pointer_b.val:
                merged_pointer.next = pointer_a
                pointer_a = pointer_a.next
            else:
                merged_pointer.next = pointer_b
                pointer_b = pointer_b.next
            merged_pointer = merged_pointer.next
        if pointer_a is not None:
            merged_pointer.next = pointer_a
        elif pointer_b is not None:
            merged_pointer.next = pointer_b
        print(4)
        return merged_dummy_head.next

    def merge(self, lists, left, right):
        print(2)
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid + 1, right)
        print(3)
        return self.merge_two_lists(l1, l2)

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        n = len(lists)
        if n == 1:
            return lists[0]
        print(1)
        return self.merge(lists, 0, n - 1)
