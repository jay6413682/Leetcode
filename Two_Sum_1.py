'''
Created on Feb 17, 2015

@author: ljiang

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        hash table 哈希表https://leetcode-cn.com/problems/two-sum/solution/liang-shu-zhi-he-by-leetcode-solution/
        时间复杂度：O(N)O(N)，其中 NN 是数组中的元素数量。对于每一个元素 x，我们可以 O(1)O(1) 地寻找 target - x。

        空间复杂度：O(N)O(N)，其中 NN 是数组中的元素数量。主要为哈希表的开销。

        """
        # {加数：index}
        hash_table = dict()
        for i, num in enumerate(nums):
            adden = target - num
            if num in hash_table:
                return [hash_table[num], i]
            hash_table[adden] = i


#!/usr/bin/env python
def two_sum(nums, target):
    for i in range(len(nums)):
        if target - nums[i] in nums:
            return i, nums.index(target - nums[i])


class Two_Sum_1:
    # @return a tuple, (index1, index2)
    
    def twoSum1(self, num, target):
        for i in xrange(len(num)):
            for j in xrange(1,len(num)):
                if num[i]+num[j]==target:
                    return (i+1,j+1)
    
    
    def twoSum2(self, num, target):
        dic={}
        for i in xrange(len(num)):
            if target - num[i] not in dic.keys():
                dic[num[i]]=i
            else:
                i1=i+1
                i2=dic[target-num[i]]+1
                return (i2,i1)
    
    def twoSum3(self, num, target):
        map = {} # maps element to its index
        for i in range(len(num)):
            if target - num[i] in map:
                i1 = i + 1
                i2 = map[target - num[i]] + 1
                return (min(i1, i2), max(i1, i2))
            else:
                map[num[i]] = i
                
    def twoSum4(self,num,target):
        for x in xrange(len(num)):
            if (target-num[x]) in num:
                return (x+1,num.index(target-num[x])+1)
            
        