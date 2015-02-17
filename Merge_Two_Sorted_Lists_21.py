'''
Created on Jul 13, 2015

@author: ljiang
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Solutions:
https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/he-bing-liang-ge-you-xu-lian-biao-by-leetcode-solu/
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionOne:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """ 双指针
        时间复杂度：O(n + m)O(n+m) ，其中 nn 和 mm 分别为两个链表的长度。因为每次循环迭代中，l1 和 l2 只有一个元素会被放进合并链表中， 因此 while 循环的次数不会超过两个链表的长度之和。所有其他操作的时间复杂度都是常数级别的，因此总的时间复杂度为 O(n+m)O(n+m)。

        空间复杂度：O(1)O(1) 。我们只需要常数的空间存放若干变量。

        """
        dummpy_node = ListNode(0)
        pointer = dummpy_node
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                pointer.next = l1
                l1 = l1.next
            else:
                pointer.next = l2
                l2 = l2.next
            pointer = pointer.next
        if l1 is None:
            pointer.next = l2
        elif l2 is None:
            pointer.next = l1
        return dummpy_node.next


class SolutionTwo:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        关于递归：https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/yi-kan-jiu-hui-yi-xie-jiu-fei-xiang-jie-di-gui-by-/
        时间复杂度：O(n + m)O(n+m)，其中 nn 和 mm 分别为两个链表的长度。因为每次调用递归都会去掉 l1 或者 l2 的头节点（直到至少有一个链表为空），函数 mergeTwoList 至多只会递归调用每个节点一次。因此，时间复杂度取决于合并后的链表长度，即 O(n+m)O(n+m)。

        空间复杂度：O(n + m)O(n+m)，其中 nn 和 mm 分别为两个链表的长度。递归调用 mergeTwoLists 函数时需要消耗栈空间，栈空间的大小取决于递归调用的深度。结束递归调用时 mergeTwoLists 函数最多调用 n+mn+m 次，因此空间复杂度为 O(n+m)O(n+m)。

        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


from LinkedList import Node,LinkedList

class Merge_Two_Sorted_List_20:
    def __init__(self,l1,l2):
        self.l1=l1
        self.l2=l2
        
    def merge(self):
        pass
        current1=self.l1.head_node
        current2=self.l2.head_node
        merged_llist=LinkedList(Node())
        merged_llist_current=merged_llist.head_node
        while current1!=None and current2!=None:
            if current1.value>current2.value:
                merged_llist_current.nxt=current1                
                current1=current1.nxt
            else:
                merged_llist_current.nxt=current2
                current2=current2.nxt
            merged_llist_current=merged_llist_current.nxt
                    
        if current1!=None:
            merged_llist_current.nxt=current1
        if current2!=None:
            merged_llist_current.nxt=current2

        merged_llist.delete(None)        
        return merged_llist           
    