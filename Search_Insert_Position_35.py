'''
Created on Jul 21, 2015

@author: ljiang
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples. [1,3,5,6],5->2 [1,3,5,6], 2->1 [1,3,5,6], 7->4 [1,3,5,6], 0->0

'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """ 模版一，binary search: O(logn); O(1) """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left


class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        模版二，binary search, binary search 通解详解:
        https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/
        O(logn);log(1)
        """
        if nums[-1] < target:
            return len(nums)
        left = 0
        right = len(nums) - 1
        # 在区间 nums[left..right] 里查找第 1 个大于等于 target 的元素的下标
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            # nums[mid] >= target，正好满足条件
            else:
                right = mid
        return right


class Solution3:
    """ 我的解，类似solution 2  这个方法不好因为最后还要判断; 看不懂就算了 """ 
    def searchInsert(self, nums: List[int], target: int) -> int:
        # less than the smallest
        if target < nums[0]:
            return 0
        left = 0
        right = len(nums) - 1
        # 在区间 nums[left..right] 里查找第 1 个大于等于 target 的元素的下标
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            # nums[mid] <= target
            else:
                left = mid
        # if there is nums[mid] == target
        if nums[left] == target:
            return left
        # if there is no nums[mid] == target
        return left + 1


class Search_Insert_Position_48:
    def __init__(self,lst,target):
        self.lst=lst
        self.target=target
    def search_and_insert(self):
        pass
        left=0
        right=len(self.lst)-1
        mid=(left+right)/2
        
        while left<right:
            if self.lst[mid] == self.target:
                return mid
            elif self.target<self.lst[mid]:
                right=mid
            elif self.target>self.lst[mid]:
                left=mid+1
            mid=(left+right)/2
                
        if self.lst[mid]>self.target:
            return mid
        else:
            return mid+1
            
                
            