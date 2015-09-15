'''
Created on Mar 19, 2015

@author: ljiang
'''
import pytest
import sys
from reverse_str_word_by_word_6 import reverse_str_word_by_word_6



@pytest.mark.parametrize("words,expectation",[("  my name is Lei ",'Lei is name my'),("my  name is    Lei",'Lei is name my'),("my name\nis Lei",False),("my name\tis Lei",False),("the sky is blue","blue is sky the"),("#@my name is&Lei",False)])     
def test_reverse_str_word_by_word(words,expectation):
    obj=reverse_str_word_by_word_6(words)
    assert obj.reverse1() == expectation
    
@pytest.mark.parametrize("words,expectation",[("  my name is Lei ",'Lei is name my'),("my  name is    Lei",'Lei is name my'),("my name\nis Lei",False),("my name\tis Lei",False),("the sky is blue","blue is sky the"),("#@my name is&Lei",False)])     
def test_reverse_str_word_by_word_2(words,expectation):
    obj=reverse_str_word_by_word_6(words)
    assert obj.reverse2() == expectation
    
    
    
@pytest.mark.parametrize("words,expectation",[("  my name is Lei ",'Lei is name my'),("my  name is    Lei",'Lei is name my'),("my name\nis Lei",False),("my name\tis Lei",False),("the sky is blue","blue is sky the"),("#@my name is&Lei",False)])     
def test_reverse_str_word_by_word_3(words,expectation):
    obj=reverse_str_word_by_word_6(words)
    assert obj.reverse3() == expectation
    
@pytest.mark.parametrize("words,expectation",[("  my name is Lei ",'Lei is name my'),("my  name is    Lei",'Lei is name my'),("my name\nis Lei",False),("my name\tis Lei",False),("the sky is blue","blue is sky the"),("#@my name is&Lei",False)])     
def test_reverse_str_word_by_word_4(words,expectation):
    obj=reverse_str_word_by_word_6(words)
    assert obj.reverse4() == expectation