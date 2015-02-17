'''
Created on Sep 21, 2015

@author: ljiang

You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contains a single digit.
Add the two numbers and return it as a linked list.

Input: (2->4->3)+(5->6->4)
Output: 7->0->8
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """ 链表，linked list, 双指针，double pointer
        https://leetcode-cn.com/problems/add-two-numbers/solution/liang-shu-xiang-jia-by-leetcode-solution/
        
        时间复杂度：O(\max(m,n))O(max(m,n))，其中 mm 和 nn 分别为两个链表的长度。我们要遍历两个链表的全部位置，而处理每个位置只需要 O(1)O(1) 的时间。

        空间复杂度：O(\max(m,n))O(max(m,n))
        """
        p1 = l1
        p2 = l2
        sum = 0
        carry = 0
        pointer = dummy = ListNode()
        while p1 is not None or p2 is not None:
            # 该位和
            if p1 is None:
                unit_sum = p2.val + carry
                p2 = p2.next
            elif p2 is None:
                unit_sum = p1.val + carry
                p1 = p1.next
            else:
                unit_sum = p2.val + p1.val + carry
                p2 = p2.next
                p1 = p1.next
            # 个位
            units = unit_sum % 10
            carry = (unit_sum - units) // 10
            pointer.next = ListNode(units)
            # print(pointer.val)
            pointer = pointer.next
        if carry == 1:
            pointer.next = ListNode(1)
        return dummy.next



from LinkedList import LinkedList, Node

def add_two_numbers(l1, l2):
    current1 = l1.head_node
    current2 = l2.head_node
    carry = 0
    dummy_head = Node()
    add_llist = LinkedList(dummy_head)
    while current1 != None or current2 != None:
        temp1 = 0
        temp2 = 0
        if current1 != None:
            temp1 = current1.value
        if current2 != None:
            temp2 = current2.value
        sum = carry + temp1 + temp2
        carry = sum / 10
        actual_val = sum % 10
        add_llist.append(actual_val)       
        if current1 != None: 
            current1 = current1.nxt
        if current2 != None:
            current2 = current2.nxt
    if carry == 1:
        add_llist.append(1)
    add_llist.delete(None)
    return add_llist
