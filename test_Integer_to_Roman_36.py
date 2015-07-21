'''
Created on Jul 16, 2015

@author: ljiang
'''
import pytest

from Integer_to_Roman_36 import Integer_to_Roman_36

@pytest.mark.parametrize("num,roman",[(11,"XI"),(6,"VI"),(49,"XLIX")])
def test_itor(num,roman):
    obj=Integer_to_Roman_36(num)
    assert obj.itor()==roman