#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
from collections import defaultdict

'''
Question: Design and implement a TwoSum class. It should support the following operations: add and find. add(input)  – Add the number input to an internal data structure. find(value) – Find if there exists any
pair of numbers which sum is equal to the value. For example, add(1); add(3); add(5); find(4)true; find(7)false
'''
from copy import deepcopy, copy


class TwoSumOne(object):
    def __init__(self):
        self.nums = list()
        self.pair_sums = defaultdict(int)

    def add(self, num):
        if not self.nums:
            self.pair_sums[num] += 1
        else:
            for n in self.nums:
                self.pair_sums[num + n] += 1
        self.nums.append(num)

    def find(self, num):
        return True if num in self.pair_sums else False


def binaray_search_insert(nums, val):
    nums = copy(nums)
    left = 0
    right = len(nums) - 1
    if len(nums) == 0:
        nums.append(val)
    else:
        while nums[left] < nums[right]:
            mid = (left + right) // 2
            if nums[mid] == val:
                nums.insert(mid, val)
                return nums
            elif val < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        nums.insert(
            left + 1, val) if nums[left] < val else nums.insert(left, val)
    return nums


class TwoSumTwo(object):
    def __init__(self):
        self.nums = []

    def add(self, num):
        self.nums = binaray_search_insert(self.nums, num)

    def find(self, target):
        i = 0
        j = len(self.nums) - 1
        while i <= j:
            if self.nums[i] + self.nums[j] == target:
                return True
            elif self.nums[i] + self.nums[j] < target:
                i += 1
            else:
                j -= 1
        return False


class TwoSumThree(object):
    def __init__(self):
        self.num_count_map = {}

    def add(self, num):
        if num not in self.num_count_map:
            self.num_count_map[num] = 1
        else:
            self.num_count_map[num] += 1

    def find(self, target):
        for count, num in enumerate(self.num_count_map):
            addend = (target - num)
            if addend in self.num_count_map:
                if addend == num and count < 2:
                    return False
                return True
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




