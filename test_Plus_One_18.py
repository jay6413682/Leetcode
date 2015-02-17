'''
Created on Jul 6, 2015

@author: ljiang
'''
import pytest

from Plus_One_18 import Plus_One_18

@pytest.mark.parametrize("lst,new_lst,func",[([9,9,9],[1,0,0,0],5),([1,2,3],[1,2,4],5),([1,2,9],[1,3,0],5),
                                             ([9,9,9],[1,0,0,0],4),([1,2,3],[1,2,4],4),([1,2,9],[1,3,0],4),
                                             ([9,9,9],[1,0,0,0],2),([1,2,3],[1,2,4],2),([1,2,9],[1,3,0],2),
                                             ([9,9,9],[1,0,0,0],3),([1,2,3],[1,2,4],3),([1,2,9],[1,3,0],3),
                                             ([9,9,9],[1,0,0,0],1),([1,2,3],[1,2,4],1),([1,2,9],[1,3,0],1)
                                             ])
def test_Plus_One_18(lst,new_lst,func):
    obj=Plus_One_18()
    if func==1:
        assert obj.Plus_One(lst,0)==new_lst
    if func==2:
        assert obj.Plus_One_2(lst)==new_lst
    if func==3:
        assert obj.Plus_One_3(lst)==new_lst
    if func==4:
        assert obj.Plus_One_4(lst)==new_lst        
    if func==5:
        assert obj.Plus_One_5(lst)==new_lst 