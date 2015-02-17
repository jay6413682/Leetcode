'''
Created on Jul 20, 2015

@author: ljiang
'''
import pytest

from FindMinSteps_DP_1 import *

@pytest.mark.parametrize("n,steps,func",[(10,3,2),(1,0,2),(4,2,2),(7,3,2),
                                         (10,3,1),(1,0,1),(4,2,1),(7,3,1)
                                         ])
def test_find_min_steps(n,steps,func):
    if func==1:
        assert find_min_step(n)==steps
    if func==2:
        assert find_min_step_2(n)==steps