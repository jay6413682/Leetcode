'''
Created on Jun 16, 2015

@author: ljiang
'''
import pytest
from Longest_Substring_with_At_Most_Two_Distinct_Characters_11 import Longest_Substring_with_At_Most_Two_Distinct_Characters_11


@pytest.mark.parametrize("n,expectation",[("eceba",3),("abcabcdabd",2),("1233212345",4),("ffffff",6),("abcbcdedf",4)])     
def test_Longest_Substring_with_At_Most_Two_Distinct_Characters_11_3(n,expectation):
    obj=Longest_Substring_with_At_Most_Two_Distinct_Characters_11()
    assert obj.Longest_Substring_with_At_Most_Two_Distinct_Characters_3(n) == expectation

@pytest.mark.parametrize("n,expectation",[("eceba",3),("aabbaacc",6),("abcabcdabd",2),("1233212345",4),("ffffff",6),("abcbcdedf",4)])     
def test_Longest_Substring_with_At_Most_Two_Distinct_Characters_11(n,expectation):
    obj=Longest_Substring_with_At_Most_Two_Distinct_Characters_11()
    assert obj.Longest_Substring_with_At_Most_Two_Distinct_Characters(n) == expectation
    
@pytest.mark.parametrize("n,expectation",[("eceba",3),("aabbaacc",6),("abcabcdabd",2),("1233212345",4),("ffffff",6),("abcbcdedf",4)])     
def test_Longest_Substring_with_At_Most_Two_Distinct_Characters_11_2(n,expectation):
    obj=Longest_Substring_with_At_Most_Two_Distinct_Characters_11()
    assert obj.Longest_Substring_with_At_Most_Two_Distinct_Characters_2(n) == expectation
    
