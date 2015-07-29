'''
Created on Feb 26, 2015

@author: ljiang
'''
import pytest
import sys
from Two_Sum_3 import *
#pytest fixture example
@pytest.fixture(scope="function",params=[0,1,2])
def config_module(request):
    try:
        print ("setup_module      module:%s" % __name__)
        if request.param == 0:
            obj=TwoSum({})
        elif request.param == 1:
            obj=TwoSum1([],[])
        elif request.param == 2:
            obj=TwoSum2([])
        def fin():
            print "teardown_module      module:%s" % __name__
            #del obj
        request.addfinalizer(fin)
        
        return obj
    except Exception,details:
        
        print details
        sys.exit(1)


@pytest.mark.parametrize("nums,target,expectation", [([-1,1,0],2,False),([100,10,0],110,True),([1,2,3,4,5],9,True),([1,1,1],2,True),([0.1,0.9],1,True)])        
def test_two_sum(config_module,nums,target,expectation):
    for element in nums:
        config_module.add(element)
    #print config_module.lst_sum
    assert config_module.find(target) == expectation

        
        