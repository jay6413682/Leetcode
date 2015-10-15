'''
Created on Oct 12, 2015

@author: ljiang
'''

import pytest

from BinarySearchTree import *

@pytest.mark.parametrize("data, expected",[([3, 2, 4, 1, 5], "3 2 4 1 5"), ([1, 2, 3, 4, 5], "1 2 3 4 5"), ([5, 4, 3, 2, 1], "5 4 3 2 1"), ([0, 1, -1, 2, -2], "0 -1 1 -2 2"), ([0, 1, -1, 2, -2], "0 -1 1 -2 2"), ([3, 2, 1, 4, 5], "3 2 4 1 5")])
def test_bft(data, expected):
    bst = BinarySearchTree(None)
    for i in data:
        bst.create(i)
    assert expected == bst.bft()

@pytest.mark.parametrize("data, expected",[([0, -2, 2, -3, -1, 1, 3], "-3 -2 -1 0 1 2 3")])
def test_inorder_ascend(data, expected):
    bst = BinarySearchTree(None)
    for i in data:
        bst.create(i)
    assert expected == bst.inorder_ascend(bst.root)

@pytest.mark.parametrize("data, expected",[([0, -2, 2, -3, -1, 1, 3], "3 2 1 0 -1 -2 -3")])
def test_inorder_descend(data, expected):
    bst = BinarySearchTree(None)
    for i in data:
        bst.create(i)
    assert expected == bst.inorder_descend(bst.root)

@pytest.mark.parametrize("data, expected",[([0, -2, 2, -3, -1, 1, 3], "0 -2 -3 -1 2 1 3")])
def test_preoder(data, expected):
    bst = BinarySearchTree(None)
    for i in data:
        bst.create(i)
    assert expected == bst.preorder(bst.root)

@pytest.mark.parametrize("data, expected",[([0, -2, 2, -3, -1, 1, 3], "-3 -1 -2 1 3 2 0")])
def test_postorder(data, expected):
    bst = BinarySearchTree(None)
    for i in data:
        bst.create(i)
    assert expected == bst.postorder(bst.root)
