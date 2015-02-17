'''
Created on Jul 12, 2015

@author: ljiang
'''
import pytest

from Palindrome_Number_19 import Palindrome_Number_19

@pytest.mark.parametrize("num,expected,func",{(12321,True,2),(123321,True,2),(-1,False,2),(124214,False,2),
                                              (12321,True,1),(123321,True,1),(-1,False,1),(124214,False,1)
                                              })
def test_Palindrome_Number_19(num,expected,func):
    obj=Palindrome_Number_19(num)
    if func==1:
        assert expected == obj.palindrome_number()
    if func==2:
        assert expected == obj.palindrome_number_2()
    