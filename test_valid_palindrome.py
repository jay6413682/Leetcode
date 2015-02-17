'''
Created on Mar 19, 2015

@author: ljiang
'''
import pytest
import sys
from Valid_Palindrome_4 import *
'''
#pytest fixture example
@pytest.fixture(scope="function",params=[0])
def config_module(request):
    try:
        print ("setup_module      module:%s" % __name__)
        obj=ValidPalindrome()
        def fin():
            print "teardown_module      module:%s" % __name__
            #del obj
        request.addfinalizer(fin)
        
        return obj
    except Exception,details:
        
        print details
        sys.exit(1)
'''

@pytest.mark.parametrize("st,expectation", [("12321",True),("abcba",True),("12a21a0919279",True),("A man, a plan, a canal: Panama",True),("race a car",False),("...AADdaa1234124",True)])        
def test_valid_palindrome(st,expectation):
    obj=ValidPalindrome(st)
    assert obj.isPalindrome() == expectation