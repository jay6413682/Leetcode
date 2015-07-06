import pytest

from Reverse_Integer_17 import Reverse_Integer_17
import sys
@pytest.mark.parametrize("i,reversed_int",[(8463847412,0),(-9463847412,0),(-123,-321),(10000000000000,1),(-100000000000000,-1),(10000000000000003,0),(123,321),(10,1),(1000,1)])
def test_Reverse_Integer_17(i,reversed_int):
    obj=Reverse_Integer_17(i)
    assert obj.Reverse_Integer()==reversed_int
    
    
