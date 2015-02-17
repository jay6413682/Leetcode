'''
Created on Jul 20, 2015

@author: ljiang
'''
import pytest
from Two_Sum_1 import Two_Sum_1

@pytest.mark.parametrize("num,target,indexes,func",[([2, 7, 11, 15], 9,(1,2),4),([11, 7, 15, 2], 9,(2,4),4),
                                                    ([2, 7, 11, 15], 9,(1,2),1),
                                                    ([2, 7, 11, 15], 9,(1,2),2),
                                                    ([2, 7, 11, 15], 9,(1,2),3)])
def test_Two_Sum_1(num,target,indexes,func):
    obj=Two_Sum_1()
    if func==1:
        assert indexes == obj.twoSum1(num, target)
    if func==2:
        assert indexes == obj.twoSum2(num, target)
    if func==3:
        assert indexes == obj.twoSum3(num, target)
    if func==4:
        assert indexes == obj.twoSum4(num, target)