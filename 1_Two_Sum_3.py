#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

'''
Created on Feb 26, 2015

@author: ljiang

Question:
Design and implement a TwoSum class. It should support the following operations: add and find.
add(input) – Add the number input to an internal data structure.
find(value) – Find if there exists any pair of numbers which sum is equal to the value.
For example,
add(1); add(3); add(5); find(4)true; find(7)false

'''

class TwoSum:
    def __init__(self,dct):
        self.dct=dct
        
    def add(self,x):
        count = self.dct[x] if self.dct.has_key(x) else 0
        self.dct.update({x:count+1})
        return 
        
    def find(self,s):
        for key,value in self.dct.items():
            target = s - key
            if target == key:
                if value >= 2:
                    return True
            else: 
                if target in self.dct.keys():
                    return True         
        return False   
