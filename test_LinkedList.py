'''
Created on Jul 13, 2015

@author: ljiang
'''
import pytest
from LinkedList import Node,LinkedList

def test_link_list_insert():    
    head=Node(0)      
    llist=LinkedList(head)
    llist.insert(1)
    assert llist.head_node.get_value()==1
    assert llist.head_node.get_next().get_value()==0
    
def test_link_list_search():
    head=Node(0)     
    llist=LinkedList(head)
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    llist.insert(4)
    
    node_found=llist.search(3)
    assert node_found.value==3
    
def test_link_list_delete():
    head=Node(0)     
    llist=LinkedList(head)
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    llist.insert(4)
    
    llist.delete(3)
    assert llist.search(3)==None

def test_link_list_size():
    head=Node(0)     
    llist=LinkedList(head)
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    llist.insert(4)
    
    assert llist.size()==5
