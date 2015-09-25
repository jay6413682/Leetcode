'''
Created on Sep 21, 2015

@author: ljiang

You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contains a single digit.
Add the two numbers and return it as a linked list.

Input: (2->4->3)+(5->6->4)
Output: 7->0->8
'''
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
