'''
Created on Jul 14, 2015

@author: ljiang
'''
import pytest

from Spiral_Matrix_35 import Spiral_Matrix_35

@pytest.mark.parametrize("matrix,result",[ ([
                                            [ 4, 5, 6 ]
                                            ],[4,5,6]),
                                          ([
                                            [ 1 ],
                                            [ 4 ],
                                            [ 7 ]
                                            ],[1,4,7]),
                                          ([
                                            [ 1, 2, 3 ],
                                            [ 4, 5, 6 ],
                                            [ 7, 8, 9 ]
                                            ],[1,2,3,6,9,8,7,4,5]),
                                          ([
                                            [ 1, 2, 3, 4],
                                            [ 4, 5, 6, 7],
                                            [ 7, 8, 9, 10]
                                            ],[1,2,3,4,7,10,9,8,7,4,5,6])])

def test_Spiral_Matrix_35(matrix, result):
    obj=Spiral_Matrix_35(matrix)
    assert obj.traverse()==result