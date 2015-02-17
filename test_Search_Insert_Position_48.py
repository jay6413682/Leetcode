'''
Created on Jul 21, 2015

@author: ljiang
'''
import pytest
from Search_Insert_Position_48 import Search_Insert_Position_48
@pytest.mark.parametrize("lst,target,index,func",[([1,3,5,6], 2,1,1),([1,3,5,6], 7,4,1),([1,3,5,6],0,0,1),([1,3,5,6],5,2,1)])
def test_Search_Insert_Position_48(lst,target,index,func):
    obj=Search_Insert_Position_48(lst,target)
    if func==1:
        assert obj.search_and_insert()==index
