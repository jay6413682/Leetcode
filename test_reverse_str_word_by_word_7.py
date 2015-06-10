'''
Created on Jun 9, 2015

@author: ljiang
'''
import pytest
import sys
from reverse_str_word_by_word_7 import reverse_str_word_by_word_7



@pytest.mark.parametrize("strg,expectation",[("abcde",'edcba'),("aabbcc",'ccbbaa'),("abcabc",'cbacba')])     
def test_reverse_str_word_by_word(strg,expectation):
    obj=reverse_str_word_by_word_7()
    assert obj.reverse_string(strg) == expectation
    
@pytest.mark.parametrize("words,expectation",[("the sky is blue","blue is sky the")])     
def test_reverse_str_word_by_word2(words,expectation):
    obj=reverse_str_word_by_word_7()
    assert obj.reverse_words(words) == expectation