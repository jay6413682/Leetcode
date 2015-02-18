'''
Created on Feb 17, 2015

@author: ljiang

Similar to Question [1. Two Sum], except that the input array is already sorted in ascending order.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
import sys
from copy import deepcopy
'''
def twoSum(num, target):
    try:
        i=0
        j=len(num)-1
        while i<j:
            if num[i]+num[j] < target:
                j+=1
            elif num[i]+num[j]== target:
                return (i+1,j+1)
            else:
                j-=1
        raise Exception("Cannot find the num in the list")
    except Exception,details:
        print details
        sys.exit()
'''
def twoSum(nums, target):
    try:
        for i in xrange(len(nums)-1):    
            index=binarySearch(target-nums[i], nums)        
            if type(index) is int:
                return (i,index)
    except Exception,details:
        print details
        sys.exit()

def binarySearch(num,lst):
    try:
        left=0
        right=len(lst)-1
        middle=(left+right)/2
        while left <=right:
            if lst[middle]==num:
                return middle
            elif lst[middle]>num:
                right=deepcopy(middle)
                middle=(left+right)/2
                
            else:
                left=deepcopy(middle)+1
                middle=(right+left)/2
        #raise Exception("Cannot find the num in the list")
    
    except Exception,details:
        print details
        sys.exit()

numbers=[2, 7, 11, 15]
target=18
print twoSum(numbers, target)