'''
Created on Mar 19, 2015

@author: ljiang
'''
import pytest
import sys
from Str_Str_5 import *



@pytest.mark.parametrize("needle,haystack,expectation", [("25","1235",False),("23",'109823',4),("23",'1234',1),("23",'23123',0),("23",'103982',False),("",'',0),("",'103982',0),("103982",'82',False),("12345678901",'',False)])        
def test_valid_palindrome(needle,haystack,expectation):
    obj=Str_Str_5(needle,haystack)
    assert obj.strStr() == expectation
    
    
@pytest.mark.parametrize("needle,haystack,expectation", [("25","1235",False),("23",'109823',4),("23",'1234',1),("23",'23123',0),("23",'103982',False),("",'',0),("",'103982',0),("103982",'82',False),("12345678901",'',False)])        
def test_valid_palindrome2(needle,haystack,expectation):
    obj=Str_Str_5(needle,haystack)
    assert obj.strStr2() == expectation
    
@pytest.mark.parametrize("needle,haystack,expectation", [("25","1235",False),("23",'109823',4),("23",'1234',1),("23",'23123',0),("23",'103982',False),("",'',0),("",'103982',0),("103982",'82',False),("12345678901",'',False)])        
def test_valid_palindrome3(needle,haystack,expectation):
    obj=Str_Str_5(needle,haystack)
    assert obj.strStr3() == expectation
    
@pytest.mark.parametrize("needle,haystack,expectation", [("103982",'82',False),("12345678901",'',False)])        
def test_valid_palindrome4(needle,haystack,expectation):
    obj=Str_Str_5(needle,haystack)
    assert obj.strStr4() == expectation
    
    
@pytest.mark.parametrize("needle,haystack,expectation", [("23",'109823',4),("25","1235",False),("23",'1234',1),("23",'23123',0),("23",'103982',False),("",'',0),("",'103982',0),("103982",'82',False),("12345678901",'',False)])        
def test_valid_palindrome5(needle,haystack,expectation):
    obj=Str_Str_5(needle,haystack)
    assert obj.strStr5() == expectation