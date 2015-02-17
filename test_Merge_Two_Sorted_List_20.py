'''
Created on Jul 13, 2015

@author: ljiang
'''
import pytest
from LinkedList import Node, LinkedList
from Merge_Two_Sorted_Lists_20 import Merge_Two_Sorted_List_20

@pytest.fixture(scope="module")
def config_module(request):
    head=Node(0)
    l1=LinkedList(head)
    l1.insert(1)
    l1.insert(2)
    l1.insert(3)
    
    head2=Node(-1)
    l2=LinkedList(head2)
    l2.insert(1)
    l2.insert(3)
    l2.insert(5)
    l2.insert(7)
    
    return l1,l2
    
def test_Merge_Two_Sorted_Lists_20(config_module):
    head=Node(-1)
    l=LinkedList(head)
    l.insert(0)
    l.insert(1)
    l.insert(1)
    l.insert(2) 
    l.insert(3)   
    l.insert(3)
    l.insert(5) 
    l.insert(7) 
    l1,l2=config_module
    obj=Merge_Two_Sorted_List_20(l1,l2)
    merged_result_llist= obj.merge()

    current1=merged_result_llist.head_node
    current2=l.head_node
    while current1!=None and current2!=None:
        if current1.value!=current2.value:
            assert False        
        current1=current1.nxt
        current2=current2.nxt
    assert True