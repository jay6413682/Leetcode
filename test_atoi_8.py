'''
Created on Jun 10, 2015

@author: ljiang
'''
import pytest
from atoi_8 import atoi_8

@pytest.mark.parametrize("strg,expectation",[(" ",0),("  ",0),("2147483647",2147483647),("-123456",-123456),("123456xyz",123456),("123456",123456),("  123456",123456),("123456   ",123456), ("  123456   ",123456),("123x456",123),("xyz123",0),("-2147483649",0),("2147483648",0),("-2147483648",-2147483648),("0",0)])     
def test_atoi(strg,expectation):
    obj=atoi_8()
    assert obj.atoi(strg) == expectation