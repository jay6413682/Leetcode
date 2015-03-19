#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

'''
Question: Design and implement a TwoSum class. It should support the following operations: add and find. add(input)  – Add the number input to an internal data structure. find(value) – Find if there exists any
pair of numbers which sum is equal to the value. For example, add(1); add(3); add(5); find(4)true; find(7)false
'''
from copy import deepcopy
class TwoSum1:
    def __init__(self,lst_sum,lst):
        self.lst_sum=lst_sum
        self.lst=lst
        
    def add(self,x):
        if len(self.lst)==0:
            self.lst.append(x)
            self.lst_sum.append(x)
        
        else:
            for element in self.lst:
                sm=x+element
                if sm not in self.lst_sum:
                    self.lst_sum.append(sm)
            self.lst.append(x)
        return 
        
    def find(self,s):
        return True if s in self.lst_sum else False

class TwoSum2:
    def __init__(self,lst):
        self.lst=lst
        
    def add(self,x):
        self.lst=sorted(self.lst)
        L=0
        if len(self.lst)==0:
            self.lst.append(x)
            return
        else: 
            R=len(self.lst)-1
            M=(L+R)/2
            while L<=R:
                if x>self.lst[R]:
                    self.lst.append(x)
                    return
                elif x<self.lst[L]:
                    self.lst.insert(M,x)
                    return
                elif x == self.lst[M] or L==R:
                    self.lst.insert(M+1,x)
                    return 
                elif x>self.lst[M]:
                    L=deepcopy(M)+1
                    M=(L+R)/2
                elif x<self.lst[M]:
                    R=deepcopy(M)
                    M=(L+R)/2
                
        return 
        
    def find(self,s):
        i=0
        j=len(self.lst)-1
        while i < j:
            if self.lst[i]+self.lst[j]==s:
                return True
            elif self.lst[i]+self.lst[j]>s:
                j-=1
            else:
                i+=1
        return False
        


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




