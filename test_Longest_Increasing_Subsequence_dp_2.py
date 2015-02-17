'''
Created on Jul 23, 2015

@author: ljiang
'''
import pytest

from LongestIncreasingSubsequence_DP_2 import LongestIncreasingSubsequence

@pytest.mark.parametrize("lst,len_longest_inc_seq",[([1,2,3,4,5,4,3,2,1],5),
                                                ([1,2,3,4,1,2,3,4],4)])
def test_LongesetIncreasingSubsequence_DP_2(lst,len_longest_inc_seq):
    obj=LongestIncreasingSubsequence(lst)
    assert obj.find_len_lis()==len_longest_inc_seq