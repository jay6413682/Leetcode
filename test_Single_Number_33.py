'''
Created on Jul 14, 2015

@author: ljiang
'''
import pytest

from Single_Number_33 import Single_Number_33

@pytest.mark.parametrize("lst,single_value,func",[([1,1,2,2,3,4,4],3,3),([-1,1,2,2,3,-1,1],3,3),
                                                  ([1,1,2,2,3,4,4],3,2),([-1,1,2,2,3,-1,1],3,2),
                                                  ([1,1,2,2,3,4,4],3,1),([-1,1,2,2,3,-1,1],3,1)
                                                  ])
def test_find_single_num(lst,single_value,func):
    obj=Single_Number_33(lst)
    if func ==1:
        assert obj.find_single_number()==single_value
    if func == 2:
        assert obj.find_single_number_2()==single_value
    if func == 3:
        assert obj.find_single_number_3()==single_value