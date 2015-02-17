'''
Created on Feb 17, 2015

@author: ljiang

Similar to Question [1. Two Sum], except that the input array is already sorted in ascending order.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
import sys
from copy import deepcopy


def twoSum2(num, target):
    try:
        i=0
        j=len(num)-1
        while i<j:
            if num[i]+num[j] < target:
                i+=1
            elif num[i]+num[j]== target:
                return (i+1,j+1)
            else:
                j-=1
        raise Exception("Cannot find the num in the list")
    except Exception as details:
        print(details)
        sys.exit()

def twoSum(nums, target):
    try:
        for i in range(len(nums)-1):
            index=binarySearch(target-nums[i], nums)        
            if type(index) is int:
                return (i+1,index+1)
    except Exception as details:
        print(details)
        sys.exit()


def recursive_binary_search(num, sorted_list, first_index, last_index):
    if first_index <= last_index:
        mid_index = (first_index + last_index) // 2
        if sorted_list[mid_index] == num:
            return mid_index
        elif num < sorted_list[mid_index]:
            return recursive_binary_search(num, sorted_list, first_index, mid_index - 1)
        else:
            return recursive_binary_search(num, sorted_list, mid_index + 1, last_index)
    else:
        return None


def two_sum(nums, target):
    for i, n in enumerate(nums):
        m = target - n
        found = iterative_binary_search(m, nums)
        if found:
            return i+1, found+1
    return


def iterative_binary_search(num, lst):
    mid_index = int((len(lst) - 1) / 2)
    first_index = 0
    last_index = len(lst) - 1
    while first_index <= last_index:
        if lst[mid_index] == num:
            return mid_index
        elif num < lst[mid_index]:
            last_index = mid_index - 1
        else:
            first_index = mid_index + 1
        mid_index = (first_index + last_index) // 2
    return


def two_sum_2(nums, target):
    i = 0
    j = len(nums) - 1
    if len(nums) == 0:
        return
    while i <= j:
        if nums[i] + nums[j] == target:
            return i + 1, j + 1
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1
    return


if __name__ == '__main__':
    numbers=[2, 7, 11, 15]
    target=18
    print(twoSum(numbers, target))