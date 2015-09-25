'''
Created on Sep 21, 2015

@author: ljiang
'''
import pytest
from LinkedList import LinkedList, Node
from Add_Two_Numbers_21 import add_two_numbers

@pytest.mark.parametrize("l1, l2, expected", [([1], [9, 9, 9], [0, 0, 0, 1]), ([1], [9, 5], [0, 6]), ([1], [4, 5], [5, 5]), ([1, 2, 3], [4, 5], [5, 7, 3]), ([1, 2, 3], [4, 5, 6], [5, 7, 9])])
def test_add_two_numbers(l1, l2, expected):
    llist1 = LinkedList(Node(l1[0]))
    llist2 = LinkedList(Node(l2[0]))
    for x in l1[1:]:
        llist1.append(x)
    for y in l2[1:]:
        llist2.append(y)
    expected_llist = add_two_numbers(llist1, llist2)
    current = expected_llist.head_node
    for z in expected:
        if current.value == z:
            current = current.nxt
            continue
        assert False
    assert True
