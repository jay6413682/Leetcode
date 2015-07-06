'''
Created on Jul 6, 2015

@author: ljiang
'''

import pytest
from Missing_Ranges_12 import Missing_Ranges_12


@pytest.mark.parametrize("lst,expected",[([],["0->99"]),([x for x in xrange(0,101)],[]),([0, 1, 3, 50, 75],["2", "4->49", "51->74", "76->99"])])
def test_Missing_Ranges_12(lst,expected):
    obj=Missing_Ranges_12(lst)
    assert expected==obj.Missing_Ranges()
