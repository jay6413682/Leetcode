'''
Created on Jun 11, 2015

@author: ljiang
'''
import pytest
from Longest_Substring_Without_Repeating_Characters_10 import Longest_Substring_Without_Repeating_Characters_10

@pytest.mark.parametrize("n,expectation",[("abcabcdabd",4),("1233212345",5),("ffffff",1),("abcbcdedf",4)])     
def test_Longest_Substring_Without_Repeating_Characters_10(n,expectation):
    obj=Longest_Substring_Without_Repeating_Characters_10()
    assert obj.Longest_Substring_Without_Repeating_Characters_2(n) == expectation
    

@pytest.mark.parametrize("n,expectation",[("abcabcdabd",4),("1233212345",5),("ffffff",1),("abcbcdedf",4)])     
def test_Longest_Substring_Without_Repeating_Characters_10_2(n,expectation):
    obj=Longest_Substring_Without_Repeating_Characters_10()
    assert obj.Longest_Substring_Without_Repeating_Characters(n) == expectation