'''
Created on Jul 21, 2015

@author: ljiang
'''

import pytest
import Two_Sum_2

@pytest.mark.parametrize("numbers,target,indexes,func",[([2, 7, 11, 15],18,(2,3),2),
                                                        ([2, 7, 11, 15],18,(2,3),1)])
def test_Two_Sum_2(numbers,target,indexes,func):
    if func==2:
        assert Two_Sum_2.twoSum2(numbers,target)==indexes
    if func==1:
        assert Two_Sum_2.twoSum(numbers,target)==indexes