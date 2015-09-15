'''
Created on Jun 11, 2015

@author: ljiang
'''
import pytest
from valid_number_9 import valid_number_9

@pytest.mark.parametrize("n,expectation",[("1.2.23",False),(" ",False),("  ",False),("1.",True),("-1.2",True),("-123456",True),("123456xyz",False),("123456",True),("+123456",True),("  123456",True),("123456   ",True), ("  123456   ",True),("123x456",False),("xyz123",False),("1.2",True),(".2",True),(".",False),("0",True)])     
def test_atoi(n,expectation):
    obj=valid_number_9()
    assert obj.valid_num(n) == expectation