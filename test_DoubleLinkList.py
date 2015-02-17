'''
Created on Sep 17, 2015

@author: ljiang
'''
import pytest
from DoubleLinkList import DoubleLinkedList
import sys

@pytest.fixture(scope = 'function')
def config_dll(request):
    '''This is to setup the double link list'''
    print "setup double linked list for all"
    dllist = DoubleLinkedList()
    def fin():
        '''This is to teardown the double link list'''
        print "teardown double linked list for all"
        #dllist = DoubleLinkedList()
    request.addfinalizer(fin)
    return dllist

@pytest.fixture(scope = 'function', params = [(1, 2, 3, 4)])
def config_dll_del_node(request, config_dll):
    '''This is to setup double linked list for unit test case test_dll_del_node'''
    print "setup double linked list for unit test case test_dll_del_node"
    dllist = config_dll
    for value in request.param:
        dllist.add_node_tail(value)
    return dllist

@pytest.mark.parametrize('value_to_add, expected',
                         [(1, 'None <--- head (tail): 1 ---> None'),
                        (2.345, 'None <--- head (tail): 2.345 ---> None'),
                        (sys.maxint, 'None <--- head (tail): %s ---> None' % sys.maxint),
                        (-sys.maxint - 1, 'None <--- head (tail): %s ---> None'
                         % (-sys.maxint - 1))])
def test_dll_add_first_value(config_dll, value_to_add, expected):
    dllist = config_dll
    dllist.add_first_value(value_to_add)
    assert dllist.display() == expected

@pytest.mark.parametrize('values_to_add, expected',
                         [([1], 'None <--- head (tail): 1 ---> None'),
                        ([1, 2, 3], '<--- head: 1 <---> node: 2 <---> tail: 3 --->'),
                        ([1, 2], '<--- head: 1 <---> tail: 2 --->')])
def test_dll_add_node_tail(config_dll, values_to_add, expected):
    dllist = config_dll
    for value in values_to_add:
        dllist.add_node_tail(value)
    assert dllist.display() == expected

@pytest.mark.parametrize('values_to_add, expected',
                         [([1], 'None <--- head (tail): 1 ---> None'),
                        ([1, 2, 3], '<--- head: 3 <---> node: 2 <---> tail: 1 --->'),
                        ([1, 2], '<--- head: 2 <---> tail: 1 --->')])
def test_dll_add_node_head(config_dll, values_to_add, expected):
    dllist = config_dll
    for value in values_to_add:
        dllist.add_node_head(value)
    assert dllist.display() == expected

@pytest.mark.parametrize('values_to_delete, expected',
                         [([4], '<--- head: 1 <---> node: 2 <---> tail: 3 --->'),
                        ([1, 2, 3, 4], 'The doubly linked list is empty.'),
                        ([1, 2, 3], 'None <--- head (tail): 4 ---> None'),
                        ([1, 2], '<--- head: 3 <---> tail: 4 --->'),
                        ([1], '<--- head: 2 <---> node: 3 <---> tail: 4 --->'),
                        ([2], '<--- head: 1 <---> node: 3 <---> tail: 4 --->'),
                        ([5], '<--- head: 1 <---> node: 2 <---> node: 3 <---> tail: 4 --->'),
                        ([5, 3], '<--- head: 1 <---> node: 2 <---> tail: 4 --->')])
def test_dll_del_node(config_dll_del_node, values_to_delete, expected):
    dllist = config_dll_del_node
    for value in values_to_delete:
        dllist.del_node(value)
    assert dllist.display() == expected
